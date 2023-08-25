def sliderAnimation(self):
    if self.is_expanded:
        self.animation_compression_max = QtCore.QPropertyAnimation(self.slider, b"maximumWidth")
        self.animation_compression_max.setDuration(800)
        self.animation_compression_max.setStartValue(230)
        self.animation_compression_max.setEndValue(0)
        self.animation_compression_max.setEasingCurve(QtCore.QEasingCurve.OutQuart)
        self.animation_compression_max.start()

        self.animation_compression_min = QtCore.QPropertyAnimation(self.slider, b"minimumWidth")
        self.animation_compression_min.setDuration(800)
        self.animation_compression_min.setStartValue(230)
        self.animation_compression_min.setEndValue(0)
        self.animation_compression_min.setEasingCurve(QtCore.QEasingCurve.OutQuart)
        self.animation_compression_min.start()
        self.is_expanded = False

    else:
        self.animation_expansion_max = QtCore.QPropertyAnimation(self.slider, b"maximumWidth")
        self.animation_expansion_max.setDuration(800)
        self.animation_expansion_max.setStartValue(0)
        self.animation_expansion_max.setEndValue(230)
        self.animation_expansion_max.setEasingCurve(QtCore.QEasingCurve.OutBack)
        self.animation_expansion_max.start()

        self.animation_compression_min = QtCore.QPropertyAnimation(self.slider, b"minimumWidth")
        self.animation_compression_min.setDuration(800)
        self.animation_compression_min.setStartValue(0)
        self.animation_compression_min.setEndValue(230)
        self.animation_compression_min.setEasingCurve(QtCore.QEasingCurve.OutBack)
        self.animation_compression_min.start()
        self.is_expanded = True


def changePage(self):
    if self.stacked_widget.currentIndex() == 0:
        self.animation_expansion_max = QtCore.QPropertyAnimation(self.page_2, b"geometry")
        self.stacked_widget.setCurrentIndex(1)
        self.animation_expansion_max.setDuration(800)
        self.animation_expansion_max.setStartValue(
            QtCore.QRect(0, -self.centralwidget.height(), self.stacked_widget.width(), self.stacked_widget.height()))
        self.animation_expansion_max.setEndValue(
            QtCore.QRect(0, 0, self.stacked_widget.width(), self.stacked_widget.height()))
        self.animation_expansion_max.setEasingCurve(QtCore.QEasingCurve.OutBack)
        self.animation_expansion_max.start()


    else:
        self.stacked_widget.setCurrentIndex(0)