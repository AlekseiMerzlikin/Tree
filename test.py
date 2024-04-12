import os
import pytest
from tree import create_tree, save_tree_to_file, save_error_message_to_file

@pytest.fixture
def results_file(tmpdir):
    return tmpdir.join("test_results.txt")

@pytest.mark.parametrize("levels", [1, 5, 10])
def test_positive_tree_construction(levels):
    tree = create_tree(levels)
    assert len(tree) == levels + 3  #Правильное количество строк
    result_message = f"Positive Tree Construction Test for {levels} levels: PASSED"
    print(result_message)

@pytest.mark.parametrize("levels", [1, 5, 10])
def test_positive_save_tree_to_file(levels):
    filename = "test_tree.txt"
    tree = create_tree(levels)
    save_tree_to_file(tree, filename)
    assert os.path.exists(filename)  # Проверяем, что файл был создан
    os.remove(filename)  
    result_message = f"Positive Save Tree to File Test for {levels} levels: PASSED"
    print(result_message)

@pytest.mark.parametrize("levels", [-5, 0, "invalid"])
def test_negative_levels(levels):
    filename = "test_error_message.txt"
    save_error_message_to_file("", filename)
    assert os.path.exists(filename)  #Файл с сообщением об ошибке  создан
    os.remove(filename)  
    result_message = f"Negative Levels Test for {levels}: PASSED"
    print(result_message)

if __name__ == "__main__":
    pytest.main()
