import argparse
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup

from . import __root__

path = __root__ / "codes"
contest_cats = ["abc", "arc", "agc", "past"]


def atcoder_parse(url: str, project: str):

    top = url[: url.find("/tasks")] if "/tasks" in url else url
    contest_cat = next(filter(lambda x: x in top.split("/")[-1], contest_cats), None)
    if contest_cat is None:
        print(f"{url}は未対応のコンテストです。{contest_cats}のいずれかが対応しています。")
        return
    res = requests.get(url=top)
    try:
        res.raise_for_status()
    except requests.HTTPError as exc:
        code = exc.response.status_code
        if code == 404:
            print(f"{url}が見つかりませんでした。")
            return

    soup = BeautifulSoup(res.text, features="html.parser")
    contest_title = soup.find("h1").text

    contest = Contest(top=top, title=contest_title, project=project)
    contest.make()


@dataclass
class Problem:
    _id: str
    title: str
    link: str

    @property
    def id(self):
        return self._id.lower()

    def generate(self, project: str, contest_cat: str, contest: str, task_url: str):
        url = task_url + f"/{self.link}"
        ios = parse_problem(url)
        params = format_param(ios)

        # tests
        with open(path / "test.txt", "r") as f:
            txt = f.read()
        txt = txt.format(
            link=url,
            title=self.title,
            path_param=f"{project}",
            path_main=f"{project}.{contest_cat}.{contest}.{self.id}",
            params=params,
        )
        test_path = Path(f"tests/{contest_cat}/{contest}/test_{contest}_{self.id}.py")
        test_path.parent.mkdir(parents=True, exist_ok=True)
        with open(test_path, "w") as f:
            f.write(txt)

        # answer
        with open(path / "answer.txt", "r") as f:
            txt = f.read()
        txt = txt.format(link=url, title=self.title)
        answer_path = Path(f"src/{project}/{contest_cat}/{contest}/{self.id}.py")
        answer_path.parent.mkdir(parents=True, exist_ok=True)
        with open(answer_path, "w") as f:
            f.write(txt)


@dataclass
class Contest:
    top: str
    title: str
    project: str = "procon"

    @cached_property
    def contest_name(self) -> str:
        return self.top.split("/")[-1]

    @cached_property
    def contest_cat(self) -> str:
        _c = next(filter(lambda x: x in self.contest_name, contest_cats), None)
        if _c is None:
            raise RuntimeError(f"{self.top}は未対応のコンテストです。{contest_cats}のいずれかが対応しています。")
        return _c

    @cached_property
    def path_src(self):
        return Path(f"./src/{self.project}/{self.contest_cat}")

    @cached_property
    def path_tests(self):
        return Path(f"./tests/{self.contest_cat}")

    @cached_property
    def problems(self) -> List[Problem]:
        res = requests.get(url=self.top + "/tasks")
        soup = BeautifulSoup(res.text, features="html.parser")
        table = soup.find("table")
        rows = table.findAll("tr")
        ps: List[Problem] = []
        for row in rows:
            cells = row.findAll(["td", "th"])
            c1 = cells[0]
            c2 = cells[1]
            a = c2.find("a")
            if a is None:
                continue
            p = Problem(_id=c1.text, title=c2.text, link=a.get("href").split("/")[-1])
            ps.append(p)
        return ps

    def make(self):
        # ディレクトリ作成
        self.path_src.mkdir(parents=True, exist_ok=True)
        self.path_tests.mkdir(parents=True, exist_ok=True)

        for problem in self.problems[:1]:
            task_url = self.top + "/tasks"
            problem.generate(
                project=self.project,
                contest_cat=self.contest_cat,
                contest=self.contest_name,
                task_url=task_url,
            )


def format_param(io: List[Tuple[List[str], List[str]]], indent_num: int = 4) -> str:
    indent = " " * indent_num
    pt = [f"Param(inputs={inp}, outputs={out})" for inp, out in io]
    pt = map(lambda x: x.replace("'", '"'), pt)
    pt = list(map(lambda x: indent * 2 + x + ",", pt))
    pt = [indent + "["] + pt + [indent + "]"]
    return "\n".join(pt)


def parse_problem(url: str) -> List[Tuple[List[str], List[str]]]:
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, "html.parser")
    inputs = []
    outputs = []
    for section in soup.find_all("section"):
        h3 = section.find("h3")
        if "Sample Input" in h3.text:
            inp: str = section.find("pre").text
            inputs.append(inp.split("\r\n")[:-1])
        if "Sample Output" in h3.text:
            out: str = section.find("pre").text
            outputs.append(out.split("\r\n")[:-1])
    return list(zip(inputs, outputs))


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", "-p", help="src直下のプロジェクトディレクトリ名", type=str, default="procon")
    parser.add_argument("url", help="問題のURL", type=str)
    args = parser.parse_args()
    atcoder_parse(url=args.url, project=args.project)
