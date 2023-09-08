from fpdf import FPDF

pdf = FPDF()
effective_page_width = pdf.w - 2 * pdf.l_margin
pdf.compress = False
pdf.add_page()
# pdf.add_font("TimesNewRoman", '', 'TimesNewRoman.ttf', uni=True)
pdf.set_font("Arial", size=30)
# pdf.cell( w=10, border =1, txt='title')
# pdf.ln(30)
# pdf.set_line_width(1)
# pdf.set_draw_color(0, 0, 0)
# pdf.line(10,20,30,40)
# pdf.set_draw_color(255, 0, 0)
# pdf.line(100,20,300,40)
# pdf.set_draw_color(255, 255, 255)
# pdf.image("./img.png", 300,100,459,270)
pdf.cell(10, 10, border=0,align='L', link=pdf.image('../img/logo/prueba.png', 4, 4, 11))

# for index_news, news_dict in enumerate(data['items']):
#     pdf.set_font("TimesNewRoman", size=20)
#     pdf.line(20, pdf.get_y() - 10, effective_page_width, pdf.get_y() - 10)
#     pdf.multi_cell(effective_page_width, 10, news_dict['title'])
#     if news_dict['contain_image']:
#         download_image_and_paste_in_pdf(pdf, news_dict, index_news)
#     pdf.multi_cell(effective_page_width, 10, news_dict['published'])
#     pdf.multi_cell(effective_page_width, 10, news_dict['summary'][news_dict['summary'].rfind(']') + 1:])
#     pdf.set_font("TimesNewRoman", size=15)
#     pdf.ln(5)
#     pdf.multi_cell(effective_page_width, 10, 'Link on news:\n' + news_dict['link'])
#     if news_dict['contain_image']:
#         pdf.multi_cell(effective_page_width, 10, 'Link on image:\n' + news_dict['link_on_image'])
#     pdf.ln(40)

# try:
pdf.output("hola.pdf", 'F')
# except PermissionError:
    # raise RssReaderException.FileException(f'close file:\n{filename}')