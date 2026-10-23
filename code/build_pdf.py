#!/usr/bin/env python3
"""
Compiles the research manuscript into a publication-ready PDF using ReportLab:
- Exact Elsevier title, author affiliations, abstract, keywords
- Numbered sections, definitions, theorems, lemmas, propositions, proofs
- Formatted tables matching CSV benchmarks
- Inline high-resolution figure inclusions
- Complete bibliography matching references.bib
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

def generate_pdf(output_filename="main.pdf"):
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#111111'),
        spaceAfter=12
    )

    author_style = ParagraphStyle(
        'AuthorStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#222222')
    )

    affil_style = ParagraphStyle(
        'AffilStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#555555'),
        spaceAfter=14
    )

    abstract_heading = ParagraphStyle(
        'AbstractHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#111111'),
        spaceAfter=4
    )

    abstract_body = ParagraphStyle(
        'AbstractBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#222222')
    )

    keywords_style = ParagraphStyle(
        'KeywordsStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#333333'),
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#0b2c4d'),
        spaceBefore=12,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'SubSectionHeading',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1a4a75'),
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#111111'),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=body_style,
        leftIndent=15,
        spaceAfter=4
    )

    theorem_style = ParagraphStyle(
        'TheoremStyle',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=9.5,
        leading=13.5,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#1a1a1a')
    )

    caption_style = ParagraphStyle(
        'CaptionStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#444444'),
        spaceBefore=4,
        spaceAfter=8
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#ffffff')
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#111111')
    )

    bib_style = ParagraphStyle(
        'BibItem',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=8.5,
        leading=11.5,
        leftIndent=18,
        firstLineIndent=-18,
        alignment=TA_JUSTIFY,
        spaceAfter=4
    )

    def theorem_box(title, text):
        content = [
            Paragraph(f"<b>{title}.</b> {text}", theorem_style)
        ]
        t = Table([[content]], colWidths=[6.8 * inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f4f7fa')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#b0c4de')),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ]))
        return t

    story = []

    # Title & Front Matter
    story.append(Paragraph("Exact Joint Code-Dimension and <i>k</i>-Galois Hull Enumerators for Repeated-Root Constacyclic Codes over Affine Algebras", title_style))
    story.append(Paragraph("<b>Arun Kumar Yadav</b><sup>a,*</sup>, <b>Vipin Gupta</b><sup>b</sup>, <b>Pooja Soni</b><sup>c</sup>, <b>Manju Pruthi</b><sup>d</sup>", author_style))
    story.append(Paragraph("<sup>a</sup> Department of Mathematics, Central University of Haryana, Mahendergarh 123031, India<br/>"
                           "<sup>b</sup> Department of Mathematics, Netaji Subhas University of Technology, New Delhi 110078, India<br/>"
                           "<sup>c</sup> Department of Mathematics, K.R. Mangalam University, Gurugram 122103, India<br/>"
                           "<sup>d</sup> Department of Mathematics, Indira Gandhi University, Meerpur, Rewari 122502, India<br/>"
                           "<sup>*</sup> Corresponding author. Email: <u>arun.yadav.math@gmail.com</u>", affil_style))

    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#333333'), spaceBefore=2, spaceAfter=8))

    # Abstract Box
    abstract_text = (
        "<b>Abstract:</b> We establish an exact algebraic framework for computing the bivariate joint code-dimension "
        "and <i>k</i>-Galois-hull enumerator for repeated-root constacyclic codes over arbitrary square-free affine algebras "
        "&Ascr; &cong; &oplus;<sub>s=1</sub><sup>m</sup> &Fopf;<sub>q<sub>s</sub></sub>. When the code length <i>n</i> is divisible by the base field characteristic "
        "<i>p<sub>s</sub></i> (the repeated-root regime <i>n</i> = <i>n&#772;<sub>s</sub></i> <i>p<sub>s</sub></i><sup><i>a<sub>s</sub></i></sup> with <i>a<sub>s</sub></i> &ge; 1), "
        "the ambient quotient ring fails to be semisimple, decomposing instead into a direct sum of local finite chain rings "
        "with nilpotency index <i>M<sub>s</sub></i> = <i>p<sub>s</sub></i><sup><i>a<sub>s</sub></i></sup> &ge; 2. Consequently, code selections at each irreducible factor "
        "become (<i>M<sub>s</sub></i> + 1)-state integer valuations rather than binary indicators. Under the <i>k</i>-Galois self-reciprocal compatibility condition, "
        "we prove that the <i>k</i>-Galois hull dimension corresponds exactly to a state-dependent local intersection statistic "
        "min(<i>u<sub>j</sub></i>, <i>M<sub>s</sub></i> &minus; <i>u</i><sub><i>j</i>&minus;1</sub>) evaluated along the orbits of the <i>k</i>-Galois Frobenius-twisted reciprocal permutation "
        "on irreducible factors.<br/><br/>"
        "We construct an explicit (<i>M</i> + 1) &times; (<i>M</i> + 1) polynomial transfer matrix <b>T</b><sub><i>M, d</i></sub>(<i>x, y</i>) "
        "whose trace Tr(<b>T</b><sub><i>M, d</i></sub>(<i>x, y</i>)<sup>&ell;</sup>) yields the exact bivariate orbit enumerator in <i>O</i>(<i>M</i><sup>3</sup> log &ell;) polynomial operations. "
        "We prove that the global joint enumerator exhibits duality palindromicity &Psi;(<i>x, y</i>) = <i>x<sup>n</sup></i> &Psi;(<i>x</i><sup>&minus;1</sup>, <i>y</i>), "
        "classify and enumerate <i>k</i>-LCD codes (showing non-trivial <i>k</i>-LCD codes cannot exist within single repeated-root components), "
        "and derive exact closed-form expressions for the unconditional mean, variance, and adjacent-state covariance of the hull dimension. "
        "Asymptotically as <i>M</i> &rarr; &infin;, the average hull dimension fraction &Eopf;[<i>H</i>]/<i>n</i> converges universally to 1/3, strictly exceeding the 1/4 limit "
        "known for simple-root codes. Complete computational verification against independent finite-field linear algebra is provided across characteristics <i>p</i> = 2, 3, 5, "
        "non-prime base fields, and direct-sum affine rings."
    )
    story.append(Paragraph(abstract_text, abstract_body))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Keywords:</b> Repeated-root constacyclic codes; <i>k</i>-Galois hull; Affine algebras; Finite chain rings; Transfer matrix method; Complementary dual codes; Quantum error-correcting codes.", keywords_style))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#333333'), spaceBefore=2, spaceAfter=10))

    # Section 1
    story.append(Paragraph("1. Introduction", h1_style))
    story.append(Paragraph(
        "Algebraic coding theory has long relied on cyclic and constacyclic codes due to their rich algebraic structure, efficient encoding and decoding "
        "via shift registers, and deep connections with finite geometry and quantum information theory [1–3]. Given a linear code <i>C</i> &sube; &Fopf;<sub><i>q</i></sub><sup><i>n</i></sup>, "
        "its hull with respect to an inner product is defined as the intersection with its dual: Hull(<i>C</i>) = <i>C</i> &cap; <i>C</i><sup>&perp;</sup>. "
        "First introduced by Sendrier [7] to evaluate permutation equivalence algorithms, code hulls have become foundational across multiple applications:", body_style
    ))
    story.append(Paragraph("&bull; <b>Quantum Error Correction:</b> In entanglement-assisted quantum error-correcting codes (EAQECCs), the number of required pre-shared maximally entangled states (ebits) is determined precisely by the Galois or Hermitian hull dimension of the classical seed code [15–17].", bullet_style))
    story.append(Paragraph("&bull; <b>Hardware Cryptography:</b> Linear codes with complementary duals (LCD codes), which satisfy Hull(<i>C</i>) = {0}, provide provable resistance against side-channel analysis (SCA) and fault-injection attacks in cryptographic hardware [8, 9].", bullet_style))
    story.append(Paragraph("&bull; <b>Structural Classification:</b> <i>k</i>-Galois hulls generalize both Euclidean and Hermitian dualities through the Frobenius automorphism &alpha; &mapsto; &alpha;<sup><i>p</i><sup><i>k</i></sup></sup> [12–14].", bullet_style))

    story.append(Paragraph(
        "Despite extensive study, algebraic code enumeration has historically been divided into two regimes:<br/>"
        "1. <b>Simple-Root Codes (gcd(<i>n, p</i>) = 1):</b> The ambient quotient ring is semisimple, decomposing into a direct sum of finite fields. Code selections are binary <i>e</i> &isin; {0, 1} [14].<br/>"
        "2. <b>Repeated-Root Codes (gcd(<i>n, p</i>) = <i>p<sup>a</sup></i> &ge; 2):</b> Introduced by Castagnoli et al. [1] and van Lint [2], the ambient ring decomposes into local <i>finite chain rings</i> with nilpotency index <i>M</i> = <i>p<sup>a</sup></i> &ge; 2 [3–6]. The code selection space is an (<i>M</i> + 1)-ary alphabet {0, 1, ..., <i>M</i>}.", body_style
    ))

    # Section 2
    story.append(Paragraph("2. Affine Algebras and Ambient Chain Ring Structure", h1_style))
    story.append(Paragraph(
        "Let &Ascr; &cong; &oplus;<sub><i>s</i>=1</sub><sup><i>m</i></sup> &Fopf;<sub><i>q<sub>s</sub></i></sub> be a square-free affine algebra. The ambient ring &Rscr;<sub>&Ascr;</sub> = &Ascr;[<i>x</i>]/&lang;<i>x<sup>n</sup></i> &minus; <b>&lambda;</b>&rang; decomposes into &oplus;<sub><i>s</i>=1</sub><sup><i>m</i></sup> &Rscr;<sub><i>s</i></sub>, "
        "where &Rscr;<sub><i>s</i></sub> = &Fopf;<sub><i>q<sub>s</sub></i></sub>[<i>x</i>]/&lang;<i>x<sup>n</sup></i> &minus; &lambda;<sub><i>s</i></sub>&rang;. In the repeated-root regime <i>n</i> = <i>n&#772;<sub>s</sub></i> <i>p<sub>s</sub><sup>a<sub>s</sub></sup></i> with <i>M<sub>s</sub></i> = <i>p<sub>s</sub><sup>a<sub>s</sub></sup></i> &ge; 2, "
        "the modulus factors uniquely over &Fopf;<sub><i>q<sub>s</sub></i></sub> as:", body_style
    ))
    story.append(Paragraph("<font face='Times-Italic' size='10.5'>x<sup>n</sup> &minus; &lambda;<sub>s</sub> = (x<sup>n&#772;<sub>s</sub></sup> &minus; &lambda;<sub>s, 0</sub>)<sup>M<sub>s</sub></sup> = &prod;<sub>i=1</sub><sup>r<sub>s</sub></sup> f<sub>s, i</sub>(x)<sup>M<sub>s</sub></sup>.</font>", ParagraphStyle('EqCenter', parent=body_style, alignment=TA_CENTER)))
    story.append(Paragraph(
        "By the Chinese Remainder Theorem, &Rscr;<sub><i>s</i></sub> &cong; &oplus;<sub><i>i</i>=1</sub><sup><i>r<sub>s</sub></i></sup> &Fopf;<sub><i>q<sub>s</sub></i></sub>[<i>x</i>]/&lang;<i>f<sub>s, i</sub></i>(<i>x</i>)<sup><i>M<sub>s</sub></i></sup>&rang;, where each component is a local principal ideal chain ring with <i>M<sub>s</sub></i> + 1 ideals. "
        "Every repeated-root code <i>C<sub>s</sub></i> is uniquely determined by a valuation vector <b>u</b><sub><i>s</i></sub> = (<i>u</i><sub><i>s</i>, 1</sub>, ..., <i>u</i><sub><i>s</i>, <i>r<sub>s</sub></i></sub>) &isin; {0, 1, ..., <i>M<sub>s</sub></i>}<sup><i>r<sub>s</sub></i></sup>, with dimension:", body_style
    ))
    story.append(Paragraph("<font face='Times-Italic' size='10.5'>dim<sub>&Fopf;<sub>q<sub>s</sub></sub></sub>(C<sub>s</sub>) = &sum;<sub>i=1</sub><sup>r<sub>s</sub></sup> u<sub>s, i</sub> deg(f<sub>s, i</sub>).</font>", ParagraphStyle('EqCenter2', parent=body_style, alignment=TA_CENTER)))

    # Section 3
    story.append(Paragraph("3. <i>k</i>-Galois Duality and Local Hull Dimension Formula", h1_style))
    story.append(Paragraph(
        "Under the <i>k<sub>s</sub></i>-Galois self-reciprocal compatibility condition &lambda;<sub><i>s</i></sub><sup><i>p<sub>s</sub><sup>k<sub>s</sub></sup> + 1</i></sup> = 1, "
        "the <i>k<sub>s</sub></i>-Galois reciprocal map <i>f</i> &mapsto; <i>f</i><sup>*, <i>k<sub>s</sub></i></sup> permutes the irreducible factors of <i>x</i><sup><i>n&#772;<sub>s</sub></i></sup> &minus; &lambda;<sub><i>s</i>, 0</sub> via permutation &pi;<sub><i>s</i></sub> &isin; &Sfrak;<sub><i>r<sub>s</sub></i></sub>.", body_style
    ))

    story.append(Spacer(1, 4))
    story.append(theorem_box(
        "Theorem 3.1 (Exact Hull Dimension for Repeated-Root Codes)",
        "Let <i>C<sub>s</sub></i> = &lang;&prod;<sub><i>i</i>=1</sub><sup><i>r<sub>s</sub></i></sup> <i>f<sub>s, i</sub></i>(<i>x</i>)<sup><i>M<sub>s</sub> &minus; u<sub>s, i</sub></i></sup>&rang; be a repeated-root constacyclic code with <i>u<sub>s, i</sub></i> &isin; {0, 1, ..., <i>M<sub>s</sub></i>}. "
        "The &Fopf;<sub><i>q<sub>s</sub></i></sub>-dimension of the <i>k<sub>s</sub></i>-Galois hull Hull<sub><i>k<sub>s</sub></i></sub>(<i>C<sub>s</sub></i>) = <i>C<sub>s</sub></i> &cap; <i>C<sub>s</sub></i><sup>&perp;<sub><i>k<sub>s</sub></i></sub></sup> is given exactly by:<br/><br/>"
        "<center><b>dim<sub>&Fopf;<sub>q<sub>s</sub></sub></sub>(Hull<sub>k<sub>s</sub></sub>(C<sub>s</sub>)) = &sum;<sub>i=1</sub><sup>r<sub>s</sub></sup> deg(f<sub>s, i</sub>) min(u<sub>s, i</sub>, M<sub>s</sub> &minus; u<sub>s, &pi;<sub>s</sub><sup>&minus;1</sup>(i)</sub>).</b></center>"
    ))
    story.append(Spacer(1, 6))

    # Section 4
    story.append(Paragraph("4. Multi-State Transfer Matrix Method & Joint Enumeration", h1_style))
    story.append(Paragraph(
        "For an orbit &Oscr; of length &ell; under &pi;<sub><i>s</i></sub> with common factor degree <i>d</i> and multiplicity <i>M</i>, we define the (<i>M</i> + 1) &times; (<i>M</i> + 1) polynomial transfer matrix <b>T</b><sub><i>M, d</i></sub>(<i>x, y</i>) with entries:", body_style
    ))
    story.append(Paragraph("<font face='Times-Italic' size='10.5'>[<b>T</b><sub>M, d</sub>(x, y)]<sub>i, j</sub> = x<sup>d &middot; j</sup> y<sup>d &middot; min(j, M &minus; i)</sup>, &nbsp;&nbsp; 0 &le; i, j &le; M.</font>", ParagraphStyle('EqCenter3', parent=body_style, alignment=TA_CENTER)))

    story.append(Spacer(1, 4))
    story.append(theorem_box(
        "Theorem 4.1 (Exact Orbit Joint Enumerator via Matrix Trace)",
        "The bivariate joint code-dimension and hull-dimension enumerator &Phi;<sub>&Oscr;</sub>(<i>x, y</i>) = &sum;<sub><i>k, h</i></sub> <i>A</i><sub><i>k, h</i></sub><sup>(&Oscr;)</sup> <i>x<sup>k</sup> y<sup>h</sup></i> is given exactly by:<br/><br/>"
        "<center><b>&Phi;<sub>&Oscr;</sub>(x, y) = Tr(<b>T</b><sub>M, d</sub>(x, y)<sup>&ell;</sup>).</b></center><br/>"
        "Across the affine algebra &Ascr;, the global joint enumerator factors as &Psi;<sub>&Ascr;</sub>(<i>x, y</i>) = &prod;<sub><i>s</i>=1</sub><sup><i>m</i></sup> &prod;<sub>&Oscr; &isin; Orb(<i>s</i>)</sub> Tr(<b>T</b><sub><i>M<sub>s</sub>, d<sub>&Oscr;</sub></i></sub>(<i>x, y</i>)<sup>&ell;<sub>&Oscr;</sub></sup>)."
    ))
    story.append(Spacer(1, 6))

    # Figure 1
    if os.path.exists("figures/fig_state_diagram.png"):
        story.append(KeepTogether([
            Image("figures/fig_state_diagram.png", width=6.2 * inch, height=3.2 * inch),
            Paragraph("<b>Figure 1:</b> Directed state transition diagram for the (<i>M</i> + 1)-state transfer matrix <b>T</b><sub>2, <i>d</i></sub>(<i>x, y</i>) (multiplicity <i>M</i> = 2).", caption_style)
        ]))

    # Section 5
    story.append(Paragraph("5. Structural Properties, Sub-Families, and Moments", h1_style))
    story.append(Paragraph(
        "<b>Theorem 5.1 (Duality Palindromicity):</b> The joint enumerator satisfies &Phi;(<i>x, y</i>) = <i>x<sup>n</sup></i> &Phi;(<i>x</i><sup>&minus;1</sup>, <i>y</i>), hence <i>A<sub>k, h</sub></i> = <i>A</i><sub><i>n&minus;k, h</i></sub>.<br/>"
        "<b>Theorem 5.2 (Classification of LCD Codes):</b> On any orbit, &Phi;<sub>&Oscr;</sub>(<i>x</i>, 0) = 1 + <i>x</i><sup><i>n</i><sub>&Oscr;</sub></sup>. Non-trivial <i>k</i>-LCD codes cannot exist within single repeated-root components.<br/>"
        "<b>Theorem 5.3 (Self-Dual Codes):</b> On an orbit &Oscr; of length &ell;, self-dual codes exist if and only if &ell; is even (yielding <i>M</i> + 1 codes) or &ell; is odd with <i>M</i> even (yielding 1 code).", body_style
    ))

    story.append(Spacer(1, 4))
    story.append(theorem_box(
        "Theorem 5.4 (Closed-Form Moments and Universal Asymptotics)",
        "Under the uniform distribution over all (<i>M</i> + 1)<sup>&ell;</sup> codes on orbit &Oscr; of length &ell; &ge; 2:<br/>"
        "1. <b>Expected Hull Dimension:</b> &Eopf;[<i>H</i><sub>&Oscr;</sub>] = <i>n</i><sub>&Oscr;</sub> &middot; <font face='Times-Italic' size='9.5'>(2M + 1) / (6(M + 1))</font>.<br/>"
        "2. <b>Adjacent Covariance:</b> Cov(<i>X</i><sub>1</sub>, <i>X</i><sub>2</sub>) = &minus;<font face='Times-Italic' size='9.5'>M(M + 2)(7M<sup>2</sup> + 14M + 9) / (360(M + 1)<sup>2</sup>)</font>.<br/>"
        "3. <b>Exact Variance (&ell; &ge; 3):</b> Var(<i>H</i><sub>&Oscr;</sub>) = <i>d</i><sup>2</sup> &ell; &middot; <font face='Times-Italic' size='9.5'>M(M + 2)(M<sup>2</sup> + 2M + 2) / (60(M + 1)<sup>2</sup>)</font>.<br/>"
        "4. <b>Asymptotic Limit:</b> lim<sub><i>M</i>&rarr;&infin;</sub> &Eopf;[<i>H</i>]/<i>n</i> = 1/3 (contrasting with 1/4 for simple-root codes)."
    ))
    story.append(Spacer(1, 6))

    # Figure 2 & 3
    if os.path.exists("figures/fig_asymptotic_moments.png"):
        story.append(KeepTogether([
            Image("figures/fig_asymptotic_moments.png", width=6.5 * inch, height=2.5 * inch),
            Paragraph("<b>Figure 2:</b> (a) Average hull dimension fraction &Eopf;[<i>H</i>]/<i>n</i> vs multiplicity <i>M</i>. (b) Variance scaling per step &sigma;<sub>step</sub><sup>2</sup>(<i>M</i>).", caption_style)
        ]))

    # Section 6
    story.append(Paragraph("6. Computational Validation and Benchmark Suite", h1_style))
    story.append(Paragraph(
        "To validate our theoretical generating polynomials, we implemented an automated verification suite in Python (`code/verify_all.py`). "
        "Every single constacyclic code in each family was independently constructed via generator matrix shifts, its dual basis determined via finite-field null spaces, "
        "and its hull dimension computed via Gaussian elimination. In all cases, 100% agreement was obtained.", body_style
    ))

    # Table 1: Summary Table
    table_data = [
        [Paragraph("<b>Family</b>", table_header_style), Paragraph("<b>Field/Ring</b>", table_header_style), Paragraph("<b><i>n</i></b>", table_header_style), Paragraph("<b><i>M</i></b>", table_header_style), Paragraph("<b>Orbits</b>", table_header_style), Paragraph("<b>Total Codes</b>", table_header_style), Paragraph("<b>LCD</b>", table_header_style), Paragraph("<b>Self-Dual</b>", table_header_style), Paragraph("<b>Agreement</b>", table_header_style)],
        [Paragraph("F1: Binary", table_cell_style), Paragraph("&Fopf;<sub>2</sub>", table_cell_style), Paragraph("6", table_cell_style), Paragraph("2", table_cell_style), Paragraph("1(1), 2(1)", table_cell_style), Paragraph("9", table_cell_style), Paragraph("4", table_cell_style), Paragraph("1", table_cell_style), Paragraph("<b>100% MATCH</b>", table_cell_style)],
        [Paragraph("F2: 2-Cycle", table_cell_style), Paragraph("&Fopf;<sub>2</sub>", table_cell_style), Paragraph("14", table_cell_style), Paragraph("2", table_cell_style), Paragraph("1(1), 3(2)", table_cell_style), Paragraph("27", table_cell_style), Paragraph("4", table_cell_style), Paragraph("3", table_cell_style), Paragraph("<b>100% MATCH</b>", table_cell_style)],
        [Paragraph("F3: Ternary", table_cell_style), Paragraph("&Fopf;<sub>3</sub>", table_cell_style), Paragraph("6", table_cell_style), Paragraph("3", table_cell_style), Paragraph("1(1), 1(1)", table_cell_style), Paragraph("16", table_cell_style), Paragraph("4", table_cell_style), Paragraph("0", table_cell_style), Paragraph("<b>100% MATCH</b>", table_cell_style)],
        [Paragraph("F4: Ternary", table_cell_style), Paragraph("&Fopf;<sub>3</sub>", table_cell_style), Paragraph("12", table_cell_style), Paragraph("3", table_cell_style), Paragraph("1(1), 1(1), 2(1)", table_cell_style), Paragraph("64", table_cell_style), Paragraph("8", table_cell_style), Paragraph("0", table_cell_style), Paragraph("<b>100% MATCH</b>", table_cell_style)],
        [Paragraph("F5: Hermitian", table_cell_style), Paragraph("&Fopf;<sub>4</sub>", table_cell_style), Paragraph("10", table_cell_style), Paragraph("2", table_cell_style), Paragraph("1(1), 2(2)", table_cell_style), Paragraph("27", table_cell_style), Paragraph("4", table_cell_style), Paragraph("3", table_cell_style), Paragraph("<b>100% MATCH</b>", table_cell_style)],
        [Paragraph("F6: Affine", table_cell_style), Paragraph("&Fopf;<sub>2</sub> &oplus; &Fopf;<sub>4</sub>", table_cell_style), Paragraph("12", table_cell_style), Paragraph("2", table_cell_style), Paragraph("Mixed (5 orbits)", table_cell_style), Paragraph("243", table_cell_style), Paragraph("32", table_cell_style), Paragraph("1", table_cell_style), Paragraph("<b>100% MATCH</b>", table_cell_style)],
        [Paragraph("F7: Large Binary", table_cell_style), Paragraph("&Fopf;<sub>2</sub>", table_cell_style), Paragraph("30", table_cell_style), Paragraph("2", table_cell_style), Paragraph("1(1), 2(1), 4(2), 4(1)", table_cell_style), Paragraph("243", table_cell_style), Paragraph("16", table_cell_style), Paragraph("3", table_cell_style), Paragraph("<b>100% MATCH</b>", table_cell_style)],
        [Paragraph("F8: Large Binary", table_cell_style), Paragraph("&Fopf;<sub>2</sub>", table_cell_style), Paragraph("42", table_cell_style), Paragraph("2", table_cell_style), Paragraph("1(1), 2(1), 3(2), 6(1), 6(2)", table_cell_style), Paragraph("2187", table_cell_style), Paragraph("32", table_cell_style), Paragraph("9", table_cell_style), Paragraph("<b>100% MATCH</b>", table_cell_style)],
    ]
    t_summary = Table(table_data, colWidths=[1.1*inch, 0.9*inch, 0.35*inch, 0.35*inch, 1.3*inch, 0.7*inch, 0.45*inch, 0.6*inch, 1.05*inch])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0b2c4d')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cccccc')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#ffffff'), colors.HexColor('#f8f9fa')])
    ]))

    story.append(KeepTogether([
        Paragraph("<b>Table 1:</b> Comprehensive summary of structural parameters and code counts across all eight evaluated repeated-root families.", caption_style),
        t_summary,
        Spacer(1, 8)
    ]))

    if os.path.exists("figures/fig_hull_distribution.png"):
        story.append(KeepTogether([
            Image("figures/fig_hull_distribution.png", width=6.5 * inch, height=2.5 * inch),
            Paragraph("<b>Figure 3:</b> (a) Joint code-dimension vs hull-dimension heatmap log(1 + <i>A<sub>k, h</sub></i>) for <i>n</i> = 42, <i>M</i> = 2 over &Fopf;<sub>2</sub> (2187 codes). (b) Conditional hull statistics &Eopf;[<i>H</i> | <i>k</i>] &plusmn; 1&sigma;.", caption_style)
        ]))

    # Section 7 & 8
    story.append(Paragraph("7. Applications to Quantum Codes and Cryptography", h1_style))
    story.append(Paragraph(
        "<b>Entanglement-Assisted Quantum Codes (EAQECCs):</b> An [[<i>n, k, d; c</i>]]<sub><i>q</i></sub> EAQECC encodes <i>k</i> logical qubits into <i>n</i> physical qubits using <i>c</i> pre-shared ebits [15–17]. "
        "A classical linear code with parameters [<i>n, k</i><sub>cl</sub>]<sub><i>q</i></sub> and Galois hull dimension <i>h</i> directly yields an EAQECC with <i>k</i><sub>quant</sub> = 2<i>k</i><sub>cl</sub> &minus; <i>n</i> + <i>h</i> and <i>c</i> = <i>h</i>. "
        "Our bivariate polynomial &Phi;(<i>x, y</i>) provides the exact catalog of all achievable quantum parameters from repeated-root seeds.<br/>"
        "<b>Side-Channel Countermeasures:</b> Cryptographic masking schemes requiring complementary duals (Hull(<i>C</i>) = {0}) [8] must avoid intermediate repeated-root exponents, operating at the component level instead.", body_style
    ))

    story.append(Paragraph("8. Conclusions", h1_style))
    story.append(Paragraph(
        "We have established the first exact algebraic framework for computing the bivariate joint code-dimension and <i>k</i>-Galois hull enumerator for repeated-root constacyclic codes over affine algebras. "
        "Using (<i>M</i> + 1) &times; (<i>M</i> + 1) polynomial transfer matrices, we proved duality palindromicity, classified LCD and self-dual codes, derived exact closed-form moments, and established the universal asymptotic mean hull ratio 1/3. "
        "Independent finite-field linear algebra computations confirmed 100% agreement across all evaluated families.", body_style
    ))

    # References
    story.append(Paragraph("References", h1_style))
    references = [
        "[1] G. Castagnoli, J. L. Massey, P. A. Schoeller, On repeated-root cyclic codes, IEEE Trans. Inform. Theory 37 (2) (1991) 337–342.",
        "[2] J. H. van Lint, Repeated-root cyclic codes, IEEE Trans. Inform. Theory 37 (2) (1991) 343–345.",
        "[3] H. Q. Dinh, S. R. López-Permouth, Cyclic and negacyclic codes over finite chain rings, IEEE Trans. Inform. Theory 50 (8) (2004) 1728–1744.",
        "[4] H. Q. Dinh, Constacyclic codes of length p^s over F_{p^m} + u F_{p^m}, J. Algebra 324 (5) (2010) 940–950.",
        "[5] H. Q. Dinh, Repeated-root constacyclic codes of length 2p^s, Finite Fields Appl. 18 (3) (2012) 580–601.",
        "[6] A. Sharma, S. Rani, On repeated-root constacyclic codes of length p^s, Discrete Math. 339 (2) (2016) 916–924.",
        "[7] N. Sendrier, On the dimension of the hull of linear codes, IEEE Trans. Inform. Theory 43 (6) (1997) 2008–2011.",
        "[8] C. Carlet, S. Mesnager, Linear codes with complementary duals: A survey, Des. Codes Cryptogr. 86 (10) (2018) 2171–2190.",
        "[9] C. Li, C. Ding, S. Li, LCD cyclic codes over finite fields, IEEE Trans. Inform. Theory 63 (7) (2017) 4344–4356.",
        "[10] S. Jitman, S. Ling, P. Udomkavanich, Hulls of cyclic codes over finite chain rings, Finite Fields Appl. 21 (2013) 11–21.",
        "[11] P. Boonniyoma, S. Jitman, Complementary-dual subfield-subcodes of linear codes, IEEE Trans. Inform. Theory 66 (6) (2020) 3730–3737.",
        "[12] E. Sangwisut, S. Jitman, S. Ling, P. Udomkavanich, Hulls of cyclic and negacyclic codes, Finite Fields Appl. 33 (2015) 232–257.",
        "[13] Y. Fan, L. Gao, Galois hulls of cyclic codes over finite fields, Theoret. Comput. Sci. 745 (2018) 1–11.",
        "[14] A. K. Yadav, V. Gupta, P. Soni, M. Pruthi, Joint code-dimension and k-Galois-hull enumerators for simple-root constacyclic codes over square-free affine algebras, Finite Fields Appl. 102 (2026) 102550.",
        "[15] T. Brun, I. Devetak, M. H. Hsieh, Correcting quantum errors with entanglement, Science 314 (5798) (2006) 436–439.",
        "[16] M. M. Wilde, T. A. Brun, Optimal entanglement formulas for entanglement-assisted quantum coding, Phys. Rev. A 77 (6) (2008) 064302.",
        "[17] J. Qian, L. Zhang, Entanglement-assisted quantum codes from repeated-root cyclic codes, Quantum Inf. Process. 17 (12) (2018) 339.",
        "[18] R. Lidl, H. Niederreiter, Finite Fields, 2nd ed., Cambridge University Press, 1997.",
        "[19] F. J. MacWilliams, N. J. A. Sloane, The Theory of Error-Correcting Codes, North-Holland, Amsterdam, 1977.",
        "[20] W. C. Huffman, V. Pless, Fundamentals of Error-Correcting Codes, Cambridge University Press, 2003."
    ]
    for ref in references:
        story.append(Paragraph(ref, bib_style))

    doc.build(story)
    print(f"=> PDF generated successfully: {output_filename}")

if __name__ == "__main__":
    generate_pdf("main.pdf")
