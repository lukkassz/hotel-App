# views/animated_button.py
from PyQt5.QtWidgets import QPushButton, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve

class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        # Set up opacity effect
        self.effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.effect)
        # Animation for opacity property
        self.opacity_anim = QPropertyAnimation(self.effect, b"opacity")
        self.opacity_anim.setDuration(200)
        self.opacity_anim.setEasingCurve(QEasingCurve.InOutQuad)

    def enterEvent(self, event):
        # Fade to lower opacity on hover
        self.opacity_anim.stop()
        self.opacity_anim.setStartValue(self.effect.opacity())
        self.opacity_anim.setEndValue(0.8)
        self.opacity_anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        # Fade back to full opacity when leaving
        self.opacity_anim.stop()
        self.opacity_anim.setStartValue(self.effect.opacity())
        self.opacity_anim.setEndValue(1.0)
        self.opacity_anim.start()
        super().leaveEvent(event)
