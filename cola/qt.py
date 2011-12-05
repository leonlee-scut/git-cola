def create_button(text='', layout=None, tooltip=None, icon=None):
    if text:
        button.setText(tr(text))
    if tooltip is not None:
        button.setToolTip(tooltip)
class DockTitleBarWidget(QtGui.QWidget):
    def __init__(self, parent, title):
        QtGui.QWidget.__init__(self, parent)
        label = QtGui.QLabel()
        font = label.font()
        font.setCapitalization(QtGui.QFont.SmallCaps)
        label.setFont(font)
        label.setText(title)

        self.close_button = QtGui.QPushButton()
        self.close_button.setFlat(True)
        self.close_button.setFixedSize(QtCore.QSize(16, 16))
        self.close_button.setIcon(qtutils.titlebar_close_icon())

        self.toggle_button = QtGui.QPushButton()
        self.toggle_button.setFlat(True)
        self.toggle_button.setFixedSize(QtCore.QSize(16, 16))
        self.toggle_button.setIcon(qtutils.titlebar_normal_icon())

        layout = QtGui.QHBoxLayout()
        layout.setMargin(2)
        layout.setSpacing(defs.spacing)
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

        self.connect(self.toggle_button, SIGNAL('clicked()'),
                     self.toggle_floating)

        self.connect(self.close_button, SIGNAL('clicked()'),
                     self.parent().toggleViewAction().trigger)

    def toggle_floating(self):
        self.parent().setFloating(not self.parent().isFloating())


    titlebar = DockTitleBarWidget(dock, title)
    dock.setTitleBarWidget(titlebar)
def create_toolbutton(text=None, layout=None, tooltip=None, icon=None):
    button = QtGui.QToolButton()
class ExpandableGroupBox(QtGui.QGroupBox):
        self.expanded = True
        self.arrow_icon_size = 16
    def set_expanded(self, expanded):
        if expanded == self.expanded:
            self.emit(SIGNAL('expanded(bool)'), expanded)
            return
        self.expanded = expanded
            widget.setHidden(not expanded)
        self.emit(SIGNAL('expanded(bool)'), expanded)
            icon_size = self.arrow_icon_size
            offset = self.arrow_icon_size + defs.spacing
            adjusted = option.rect.adjusted(0, 0, -offset, 0)
            top_left = adjusted.topLeft()
            self.set_expanded(not self.expanded)
        painter.translate(self.arrow_icon_size + defs.spacing, 0)
        painter.drawText(option.rect, QtCore.Qt.AlignLeft, self.title())
        point = option.rect.adjusted(0, -4, 0, 0).topLeft()
        icon_size = self.arrow_icon_size
        if self.expanded:
        else:
            painter.drawPrimitive(style.PE_IndicatorArrowRight, option)
def rgba(r, g, b, a=255):
    c = QColor()
    c.setRgb(r, g, b)
    c.setAlpha(a)
    return c
    'color_text':           rgba(0x00, 0x00, 0x00),
    'color_add':            rgba(0xcd, 0xff, 0xe0),
    'color_remove':         rgba(0xff, 0xd0, 0xd0),
    'color_header':         rgba(0xbb, 0xbb, 0xbb),
        diff_head = self.mkformat(fg=self.color_header)
        diff_head_bold = self.mkformat(fg=self.color_header, bold=True)
        diff_add = self.mkformat(fg=self.color_text, bg=self.color_add)
        diff_remove = self.mkformat(fg=self.color_text, bg=self.color_remove)
            bad_ws = self.mkformat(fg=Qt.black, bg=Qt.red)
        diff_old_rgx = TERMINAL(r'^--- a/')
        diff_new_rgx = TERMINAL(r'^\+\+\+ b/')
        diff_ctx_rgx = TERMINAL(r'^@@ ')

        diff_hd1_rgx = TERMINAL(r'^diff --git a/.*b/.*')
        diff_hd2_rgx = TERMINAL(r'^index \S+\.\.\S+')
        diff_hd3_rgx = TERMINAL(r'^new file mode')
        diff_add_rgx = TERMINAL(r'^\+')
        diff_rmv_rgx = TERMINAL(r'^-')
        diff_bar_rgx = TERMINAL(r'^([ ]+.*)(\|[ ]+\d+[ ]+[+-]+)$')
        diff_sts_rgx = (r'(.+\|.+?)(\d+)(.+?)([\+]*?)([-]*?)$')
        diff_sum_rgx = (r'(\s+\d+ files changed[^\d]*)'
                        r'(:?\d+ insertions[^\d]*)'
                        r'(:?\d+ deletions.*)$')

        self.create_rules(diff_old_rgx,     diff_head,
                          diff_new_rgx,     diff_head,
                          diff_ctx_rgx,     diff_head_bold,
                          diff_bar_rgx,     (diff_head_bold, diff_head),
                          diff_sts_rgx,     (None, diff_head,
                                             None, diff_head,
                                             diff_head),
                          diff_sum_rgx,     (diff_head,
                                             diff_head,
                                             diff_head))
            font.setPointSize(12)