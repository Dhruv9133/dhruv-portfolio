from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, ListFlowable, ListItem


NAME = "Dhruv Swami"
EMAIL = "dhruvswami9133@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/dhruv-swami/"
GITHUB = "https://github.com/Dhruv9133"


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="ResumeTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="ResumeRole",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#0f766e"),
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="SectionHeader",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#0f766e"),
        spaceBefore=8,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="ItemTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#111827"),
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.2,
        leading=14,
        textColor=colors.HexColor("#374151"),
    )
)


def bullet_list(items):
    return ListFlowable(
        [
            ListItem(Paragraph(item, styles["Body"]), leftIndent=8)
            for item in items
        ],
        bulletType="bullet",
        start="circle",
        leftIndent=16,
    )


def add_section(story, title):
    story.append(Spacer(1, 0.12 * inch))
    story.append(Paragraph(title, styles["SectionHeader"]))


def add_experience_block(story, title, bullets):
    story.append(Paragraph(title, styles["ItemTitle"]))
    story.append(bullet_list(bullets))
    story.append(Spacer(1, 0.08 * inch))


def build_pdf(path, role, summary, skills, experiences, projects):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        rightMargin=42,
        leftMargin=42,
        topMargin=36,
        bottomMargin=36,
        title=f"{NAME} Resume",
        author=NAME,
    )

    story = [
        Paragraph(NAME, styles["ResumeTitle"]),
        Paragraph(role, styles["ResumeRole"]),
        Paragraph(
            f"{EMAIL} | {LINKEDIN} | {GITHUB}",
            styles["Body"],
        ),
        Spacer(1, 0.16 * inch),
    ]

    add_section(story, "Professional Summary")
    story.append(Paragraph(summary, styles["Body"]))

    add_section(story, "Technical Skills")
    story.append(Paragraph(skills, styles["Body"]))

    add_section(story, "Experience")
    for title, bullets in experiences:
      add_experience_block(story, title, bullets)

    add_section(story, "Projects")
    for title, bullets in projects:
      add_experience_block(story, title, bullets)

    add_section(story, "Education")
    story.append(
        Paragraph(
            "Bachelor’s Degree in Computer Science, SRM University, Chennai | 2022 – 2026 | CGPA: 7.71",
            styles["Body"],
        )
    )

    doc.build(story)


build_pdf(
    "Dhruv_Swami_SDE_Resume.pdf",
    "Software Development Engineer | Frontend Developer",
    (
        "Computer Science undergraduate with knowledge of Frontend Development, Web "
        "Development, and software engineering concepts. Skilled in Python, MySQL, "
        "HTML, CSS, React, GitHub, and REST APIs. Strong problem-solving, "
        "communication, and teamwork skills with the ability to learn quickly and "
        "work in fast-paced environments."
    ),
    "Python, MySQL, PostgreSQL, HTML, CSS, React, REST APIs, GitHub, Postman, Problem Solving, Teamwork",
    [
        (
            "Freelance Web Developer | Education Sector Project | Jan 2026",
            [
                "Designed and developed a responsive school website using HTML and CSS.",
                "Managed website structure, content, and user-friendly navigation.",
                "Worked directly with clients to understand requirements and deliver solutions.",
                "Improved website performance and usability for better user experience.",
            ],
        ),
        (
            "Jobipo | Data Analyst Intern | Mar 2026 – Jun 2026",
            [
                "Collaborated with team members to improve workflows and reporting processes.",
                "Worked in a team environment with strong focus on communication and problem solving.",
                "Applied SQL and Python on business datasets, strengthening engineering and analytical workflows.",
            ],
        ),
    ],
    [
        (
            "Employee Management System",
            [
                "Developed a Full-Stack Employee Management System for managing employee records.",
                "Implemented CRUD operations, authentication, and database connectivity.",
                "Worked with frontend and backend technologies to build a user-friendly system.",
            ],
        ),
        (
            "Human Action Recognition",
            [
                "Developed a Human Action Recognition system using Machine Learning and Computer Vision techniques.",
                "Processed video datasets and trained models to identify human activities.",
            ],
        ),
        (
            "DeepShield – Deepfake Image Detection System",
            [
                "Developed a deepfake image detection system using deep learning techniques.",
                "Improved prediction transparency using Grad-CAM visualizations.",
            ],
        ),
    ],
)

build_pdf(
    "Dhruv_Swami_Data_Analyst_Resume.pdf",
    "Data Analyst",
    (
        "Computer Science undergraduate with knowledge of Data Analysis, SQL, Python, "
        "dashboards, and reporting workflows. Skilled in Python, SQL, MySQL, Excel, "
        "Power BI, and business reporting. Strong analytical thinking, communication, "
        "and teamwork skills with the ability to clean data, identify trends, and "
        "support data-driven decisions."
    ),
    "Python, SQL, MySQL, PostgreSQL, Excel, Power BI, Data Analysis, Data Cleaning, Reporting, Dashboards, GitHub",
    [
        (
            "Jobipo | Data Analyst Intern | Mar 2026 – Jun 2026",
            [
                "Collected, cleaned, and analyzed large datasets using SQL and Python.",
                "Worked on business reports and dashboards using Excel and Power BI.",
                "Identified trends and insights to support business decisions.",
                "Collaborated with team members to improve workflows and reporting processes.",
            ],
        ),
        (
            "PrepInsta | Data Analyst Intern | Dec 2023 – Feb 2024",
            [
                "Worked with datasets using SQL, Excel, and Python for analysis and reporting.",
                "Created reports and dashboards to present business insights clearly.",
                "Supported data-driven decision-making through analytical findings.",
                "Improved data quality through cleaning and preprocessing techniques.",
            ],
        ),
    ],
    [
        (
            "Sales Performance Dashboard",
            [
                "Built an interactive Power BI dashboard to analyze sales performance, returns, and delivery delays.",
                "Designed KPI cards to track total sales, total orders, average delivery delay, and return rates.",
                "Presented insights through clear dashboards for better decision-making.",
            ],
        ),
        (
            "Customer Shopping Behavior Analysis",
            [
                "Analyzed customer shopping data to understand purchasing behavior and sales trends.",
                "Used SQL queries to identify top customers, best-selling products, and revenue patterns.",
                "Created interactive Power BI dashboards to visualize insights and business performance.",
            ],
        ),
        (
            "DeepShield – Deepfake Image Detection System",
            [
                "Used Python and Machine Learning libraries for model training and evaluation.",
                "Improved prediction transparency using Grad-CAM visualizations.",
            ],
        ),
    ],
)
