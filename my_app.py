#!/usr/bin/env python3
import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
from demos import intro, crystal, metal, ion

LOGGER = get_logger(__name__)

# Dictionary of
# demo_name -> (demo_function, demo_description)
DEMOS = OrderedDict(
    [
        (
            "首页",
            (
                intro.intro,
                """
                """
            )
        ),
        (
            "第7章 晶体的点阵结构和晶体的性质",
            (
                crystal. crystal,
                """
                本节整理了晶体相关的内容
                """
            )
        ),
        (
            "第8章 金属的结构和性质",
            (
                metal. metal,
                """
                本节整理了金属相关的内容
                """
            )
        ),
        (
            "第9章 离子化合物的结构化学",
            (
                ion. ion,
                """
                本节整理了离子化合物相关的内容
                """
            )
        )
    ]
)


def run():
    demo_name = st.sidebar.selectbox("Choose a chapter", list(DEMOS.keys()), 0)
    demo = DEMOS[demo_name][0]

    if demo_name == "首页":
        show_code = False
        st.write("# 结构化学笔记")
    else:
        show_code = st.sidebar.checkbox("Show code", False)
        st.markdown("# %s" % demo_name)
        description = DEMOS[demo_name][1]
        if description:
            st.write(description)
        # Clear everything from the intro page.
        # We only have 4 elements in the page so this is intentional overkill.
        for i in range(10):
            st.empty()

    demo()

    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    run()
