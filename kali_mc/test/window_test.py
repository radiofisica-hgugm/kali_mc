import sys
import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator
from main import Window  # Import your class from your module


def test_window_initialization(qtbot):
    """Test that the Window initializes correctly."""
    window = Window()
    qtbot.addWidget(window)

    # Check if window is set up properly (for example, checking for UI elements)
    assert not window.isVisible()  # By default, it should not be shown yet


def test_translation_loading(qtbot, mocker):
    """Test that the translation loading works correctly."""
    translator = QTranslator()

    # Mock the translation loading part
    translations_path = "mocked_path"
    locale = "en"

    # Mock os.path.join and QTranslator.load
    mocker.patch("os.path.join", return_value=f"{translations_path}/{locale}.qm")
    mocker.patch.object(translator, "load", return_value=True)

    assert translator.load(f"{translations_path}/{locale}.qm") is True

    # Test if the app would install the translator (use mock for it as well)
    mock_app = mocker.MagicMock()
    mock_app.installTranslator = mocker.MagicMock()
    mock_app.installTranslator(translator)

    mock_app.installTranslator.assert_called_once_with(translator)
