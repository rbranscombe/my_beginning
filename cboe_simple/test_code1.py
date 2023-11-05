#test_code1.py

from textwrap import dedent

import pytest

import code1

MODBASE = "code1"

def test_data(mocker,capsys,tmp_path):
    #Arrange
    fake_path1 = tmp_path / "data1.txt"
    fake_path2 = tmp_path / "data2.txt"
    fake_path1.write_text(
        dedent(
            """\
            1:10
            5:25
            7:28
            10:14
            """
            )
        )
    fake_path2.write_text(
        dedent(
            """\
            0:4
            1:9
            4:79
            8:1
            9:29
            10:5
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
    code1.main()
    #Assert
    out, err = capsys.readouterr()
    expected = dedent(
        """\
        1:10,9
        10:14,5
        """
    )
    assert out == expected

def test_with_duplicates(mocker,capsys,tmp_path):
    #Arrange
    fake_path1 = tmp_path / "data1.txt"
    fake_path2 = tmp_path / "data2.txt"
    fake_path1.write_text(
        dedent(
            """\
            1:10
            1:11
            5:25
            7:28
            10:-1
            10:14
            """
            )
        )
    fake_path2.write_text(
        dedent(
            """\
            0:4
            1:9
            4:79
            8:1
            9:29
            10:5
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
    code1.main()
    #Assert
    out, err = capsys.readouterr()
    expected = dedent(
        """\
        1:10,11,9
        10:-1,14,5
        """
    )
    assert out == expected
