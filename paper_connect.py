from Document_Parsing.document_parsing import read_pdf
from Text_Processing.textprocess import get_common_graph

exctracted_text = read_pdf("paper2.pdf")
get_common_graph(exctracted_text)