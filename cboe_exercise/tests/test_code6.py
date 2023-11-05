from textwrap import dedent

import pytest

import code6

MODBASE = "code6"

def test_simple(mocker, capsys, tmp_path):
    #Setup
    fake_path1 = tmp_path / "data1.txt"
    fake_path2 = tmp_path / "data2.txt"
    fake_path1.write_text(
        dedent(
            """\
            1:32
            4:78
            7:21
            9:3
            """
        )
    )

    fake_path2.write_text(
        dedent(
            """\
            0:4
            4:79
            4:80
            8:1
            9:29
            10:-1
            """
        )
    )
    mocker.patch(
        MODBASE + ".filename1",
        fake_path1,
    )
    mocker.patch(
        MODBASE + ".filename2",
        fake_path2,   
    )

    #Run
    code6.main()

    #verify
    out, err = capsys.readouterr()
    expected = dedent(
        """\
        4:78,79,80
        9:3,29
        """
    )
    assert out == expected
