def changePage(self, page, index):
    if self.stacked_widget.currentIndex() == 0:
        self.animation_expansion_max = QtCore.QPropertyAnimation(self.page_2, b"geometry")
        self.stacked_widget.setCurrentIndex(1)
        self.animation_expansion_max.setDuration(800)
        self.animation_expansion_max.setStartValue(
            QtCore.QRect(0, -self.central_widget.height(), self.stacked_widget.width(),
                         self.stacked_widget.height()))
        self.animation_expansion_max.setEndValue(
            QtCore.QRect(0, 0, self.stacked_widget.width(), self.stacked_widget.height()))
        self.animation_expansion_max.setEasingCurve(QtCore.QEasingCurve.OutBack)
        self.animation_expansion_max.start()

    else:
        self.stacked_widget.setCurrentIndex(0)