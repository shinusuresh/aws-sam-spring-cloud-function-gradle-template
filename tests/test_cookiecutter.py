"""
    Tests cookiecutter baking process and rendered content
"""
import pytest


def test_project_tree(cookies):
    result = cookies.bake(extra_context={"group_id": "com.demo", "artifact_id": "app"})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "app"
    assert result.project_path.is_dir()
    assert result.project_path.joinpath("template.yaml").is_file()
    assert result.project_path.joinpath("README.md").is_file()
    assert result.project_path.joinpath("src").is_dir()
    assert result.project_path.joinpath("src", "main").is_dir()
    assert result.project_path.joinpath("src", "main", "java").is_dir()
    assert result.project_path.joinpath("src", "main", "java", "com").is_dir()
    assert result.project_path.joinpath("src", "main", "java", "com", "demo", "app", "FunctionApplication.java").is_file()
    assert result.project_path.joinpath("src", "test", "java", "com", "demo", "app", "FunctionApplicationTests.java").is_file()
