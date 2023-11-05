#test_code1.py

from textwrap import dedent

import pytest

import code1

MODBASE = "code1"

def test_code(
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

            
    #Act
    code1.main()
    
    #Assert
    out, err = capsys.readouterr()
    expected = dedent(
        """\
        4:78,79,80
        9:3,29
        """
    )
    assert out == expected
