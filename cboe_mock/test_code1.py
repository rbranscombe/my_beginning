#test_code1.py

from textwrap import dedent

import pytest

import code1

MODBASE = "code1"

def test_simple(mocker,capsys,tmp_path):
    #Arrange
    fake_path1 = tmp_path / "data1.txt"
    fake_path2 = tmp_path / "data2.txt"
    fake_path1.write_text(
        dedent(
            """\
            1:12
            2:13
            4:78
            7:21
            8:-1
            9:3
            """
            )
        )
    fake_path2.write_text(
        dedent(
            """\
            0:4
            1:10
            8:15
            10:-1
            11:14
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
        1:12,10
        8:-1,15
        """
    )
    assert out == expected

def test_duplicates(mocker,capsys,tmp_path):
    #Arrange
    fake_path1 = tmp_path / "data1.txt"
    fake_path2 = tmp_path / "data2.txt"
    fake_path1.write_text(
        dedent(
            """\
            1:12
            2:13
            4:78
            7:21
            8:-1
            9:3
            """
            )
        )
    fake_path2.write_text(
        dedent(
            """\
            0:4
            1:10
            1:11
            8:15
            10:-1
            11:14
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
        1:12,10,11
        8:-1,15
        """
    )
    assert out == expected


        
