# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

INK = colors.HexColor("#0f172a")
INK_SOFT = colors.HexColor("#5b6b82")
ACCENT = colors.HexColor("#2454c9")
TEAL = colors.HexColor("#0d8f83")
BORDER = colors.HexColor("#d8dfe8")

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=20, textColor=INK, leading=23, spaceAfter=2),
    "tagline": ParagraphStyle("tagline", fontName="Helvetica", fontSize=10, textColor=ACCENT, leading=12.5, spaceAfter=4),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8.7, textColor=INK_SOFT, leading=12),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT, spaceBefore=6, spaceAfter=3, leading=13),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.1, textColor=INK, leading=12.6, spaceAfter=3),
    "body_soft": ParagraphStyle("body_soft", fontName="Helvetica", fontSize=8.8, textColor=INK_SOFT, leading=12, spaceAfter=2),
    "item_title": ParagraphStyle("item_title", fontName="Helvetica-Bold", fontSize=9.6, textColor=INK, leading=12.5, spaceAfter=1),
    "item_meta": ParagraphStyle("item_meta", fontName="Helvetica-Oblique", fontSize=8.4, textColor=TEAL, leading=11, spaceAfter=2),
}

def hr():
    return HRFlowable(width="100%", thickness=0.6, color=BORDER, spaceBefore=1, spaceAfter=4)

def build():
    doc = SimpleDocTemplate(
        "Monique_Marrafon_CV.pdf", pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm, topMargin=10 * mm, bottomMargin=10 * mm,
        title="Monique Marrafon - CV", author="Monique Marrafon",
    )
    story = []

    story.append(Paragraph("Monique Marrafon", styles["name"]))
    story.append(Paragraph(
        "Estudante de Programação e Sistemas de Informação (CET &ndash; IEFP) | Cibersegurança &amp; Pentest (Solyd One)",
        styles["tagline"]))
    story.append(Paragraph(
        "Vila Nova de Gaia, Portugal &nbsp;&middot;&nbsp; marrafonmonique7@gmail.com &nbsp;&middot;&nbsp; +351 929 278 028 "
        "&nbsp;&middot;&nbsp; moniquemarrafon.github.io &nbsp;&middot;&nbsp; github.com/moniquemarrafon "
        "&nbsp;&middot;&nbsp; linkedin.com/in/moniquemarrafon",
        styles["contact"]))
    story.append(Spacer(1, 2))
    story.append(hr())

    # Perfil
    story.append(Paragraph("PERFIL", styles["h2"]))
    story.append(Paragraph(
        "Profissional em transição de carreira para a área de Tecnologia da Informação, atualmente a concluir o "
        "<b>CET em Tecnologias e Programação de Sistemas de Informação</b> (IEFP) e em formação complementar em "
        "<b>Cibersegurança e Pentest</b> (em andamento) pela Solyd One. Interesse em desenvolvimento backend e "
        "segurança da informação, com autonomia de aprendizagem e prática constante em Python, Linux e redes. "
        "Procura uma oportunidade de estágio onde possa aplicar e continuar a desenvolver os conhecimentos adquiridos.",
        styles["body"]))

    # Formação
    story.append(Paragraph("FORMAÇÃO", styles["h2"]))
    story.append(Paragraph("CET &ndash; Tecnologias e Programação de Sistemas de Informação", styles["item_title"]))
    story.append(Paragraph("IEFP &middot; Em andamento &middot; Previsão de conclusão: maio de 2027", styles["item_meta"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Cibersegurança e Pentest", styles["item_title"]))
    story.append(Paragraph("Solyd Offensive Security (Solyd One) &middot; Em andamento", styles["item_meta"]))
    story.append(Paragraph(
        "Trilhas em curso: Fundamentos de Pentest (Absoluto Zero), Segurança em Aplicações Web/Cloud/Mobile, "
        "Pentest em Ambientes Windows/Active Directory. Certificações em preparação: SYAP e SYES.",
        styles["body"]))

    # Competencias
    story.append(Paragraph("COMPETÊNCIAS TÉCNICAS", styles["h2"]))
    skills = [
        ("Programação", "Python, Lógica de Programação"),
        ("Bases de Dados", "SQL"),
        ("Sistemas &amp; Redes", "Linux, Redes de Computadores"),
        ("Desenvolvimento Web", "HTML, CSS"),
        ("Controlo de Versões", "Git, GitHub"),
        ("Cibersegurança / Pentest", "Fundamentos de Segurança da Informação, Criptografia, Reconhecimento (Recon), "
                                      "Segurança em Aplicações Web, Active Directory"),
    ]
    rows = []
    for label, val in skills:
        rows.append([
            Paragraph(f"<b>{label}</b>", styles["body"]),
            Paragraph(val, styles["body_soft"]),
        ])
    t = Table(rows, colWidths=[42 * mm, 118 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(t)

    # Projetos
    story.append(Paragraph("PROJETOS", styles["h2"]))
    story.append(Paragraph("Scanner de Pentest &ndash; Controlo de Servidor", styles["item_title"]))
    story.append(Paragraph("Python &middot; requests &middot; BeautifulSoup4 &middot; tkinter", styles["item_meta"]))
    story.append(Paragraph(
        "Ferramenta educativa que simula um ataque completo contra um servidor vulnerável (DVWA), explorando "
        "Command Injection: reconhecimento, scan de rede, scan de portas e controlo do servidor.",
        styles["body"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Sistema de Reconhecimento Facial", styles["item_title"]))
    story.append(Paragraph("Python &middot; OpenCV &middot; InsightFace &middot; NumPy", styles["item_meta"]))
    story.append(Paragraph(
        "Sistema de segurança com reconhecimento facial em tempo real: deteção de rosto, extração de embedding, "
        "reconhecimento de utilizadores registados e registo de tentativas de acesso em log.",
        styles["body"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Linux Commands Cheat Sheet", styles["item_title"]))
    story.append(Paragraph("Python 3.11 &middot; github.com/moniquemarrafon/linux-commands-cheat-sheet", styles["item_meta"]))
    story.append(Paragraph(
        "Cheat sheet interativo de comandos Linux, com 17 categorias e busca por palavra-chave em todas as "
        "categorias simultaneamente.",
        styles["body"]))

    # Experiencia
    story.append(Paragraph("EXPERIÊNCIA COMPLEMENTAR", styles["h2"]))
    exp = [
        ("Operadora de Caixa / Repositora",
         "Atendimento ao cliente em ambiente de grande movimento; operação de caixa com responsabilidade na "
         "gestão de valores; reposição e organização de mercadorias; trabalho em equipa."),
        ("Operadora de Cobrança",
         "Atendimento telefónico a clientes; negociação e acompanhamento de pagamentos; atualização de "
         "informações em sistemas informáticos; comunicação clara e resolução de situações administrativas."),
        ("Auxiliar de Cozinha",
         "Preparação e organização de pedidos; cumprimento de normas de higiene e segurança alimentar; "
         "trabalho em equipa em ambiente de elevada pressão."),
    ]
    for title, desc in exp:
        story.append(Paragraph(title, styles["item_title"]))
        story.append(Paragraph(desc, styles["body_soft"]))
        story.append(Spacer(1, 2))

    # Idiomas
    story.append(Paragraph("IDIOMAS", styles["h2"]))
    story.append(Paragraph("Português &ndash; Nativo &nbsp;&nbsp;&middot;&nbsp;&nbsp; Inglês &ndash; Intermédio", styles["body"]))

    doc.build(story)
    print("done")

if __name__ == "__main__":
    build()
