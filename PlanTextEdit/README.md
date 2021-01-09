# `QPlanTextEdit`

Text Editor that can be used to for displaying the contents (vast).

More advanced and optimized than the `QTextEdit`. [More on this](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QPlainTextEdit.html#differences-to-qtextedit)

## Some Basic Methods

  ### * `setPlainText(x)`: replaces the entire preexisting string with the x (`str()` or its eqivalent)

  ### * `paste()`: for copying the data in clipboard at the current cursor point.

  ### * [key bindings](https://doc.qt.io/qtforpython/PySide6/QtWidgets/QPlainTextEdit.html#editing-key-bindings)

  ### * `insertPlainText(str)` and `isnertHtml(html)` appends the plaintext and HTML (from the viewport of the current cursor position).

  ### * `setReadOnly()` sets the text editor to read only mode and `readOnly()` returns whether it's readonly or not.

  ### * `setPlaceholderText()` sets the placeholder text. and `placeholderText()` returns the placeholder text of the Textedit.