from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScroller, QTableWidget


def enable_table_touch_scrolling(table, hscroll=False, vscroll=False):
    QScroller.grabGesture(table, QScroller.ScrollerGestureType.TouchGesture)
    if not hscroll:
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    if not vscroll:
        table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    table.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
    table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
