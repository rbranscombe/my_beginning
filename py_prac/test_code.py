from textwrap import dedent

import pytest

from . import code

MODBASE = "code"

def test_integration(
        mocker,
        capsys,
        tmp_path
):
    #Arrange
    fake_path1 = tmp_path / "data1.txt"
    fake_path2 = tmp_path / "data2.txt"
    fake_path1.write_text(
        dedent(
            """\
            4.78
            9:3
            """
            )
        )
    fake_path2.write_text(
        dedent(
            """\
            4.79
            4:80
            9:29
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
    #Act
    code.main()
    #Assert
    out, err = capsys.readouterr()
    expected = dedent(
        """\
        4:78,79
        9:29
        """
    )
    assert out == expected
