import os.path
from fpdf import FPDF


class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.generate()

    @classmethod
    def get(cls):
        name = input('Name: ').strip()
        return cls(name)

    def generate(self):
        dir = os.path.dirname(__file__)
        shirtificate = os.path.join(dir, 'shirtificate.png')

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.set_font('helvetica', size=48)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=50, txt='CS50 Shirtificate', align='C')
        pdf.ln()

        pdf.image(shirtificate, x=10, y=70, w=190)

        pdf.set_font('helvetica', size=24)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(w=0, h=150, txt=f'{self.name} took CS50', align='C')
        pdf.ln()

        pdf.output(os.path.join(dir, 'shirtificate.pdf'))


def main():
    Shirtificate.get()


if __name__ == '__main__':
    main()
