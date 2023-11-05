from textwrap import dedent

import pytest

import cboe_merge


MODBASE = "cboe_merge"


class TestCboeMerge:

    def test_integration(self, mocker, tmp_path, capsys):
        # Arrange.
        mocker.patch(MODBASE + ".filename1", tmp_path / "filename1.txt")
        mocker.patch(MODBASE + ".filename2", tmp_path / "filename2.txt")
        (tmp_path / "filename1.txt").write_text(
            dedent(
                """\
                1:32
                2:57
                3:17
                """
            ),
        )
        (tmp_path / "filename2.txt").write_text(
            dedent(
                """\
                1:41
                3:92
                """
            ),
        )
        # Act.
        cboe_merge.main()
        # Assert.
        out, err = capsys.readouterr()
        assert out == dedent(
            """\
            1:32,41
            3:17,92
            """
        )
