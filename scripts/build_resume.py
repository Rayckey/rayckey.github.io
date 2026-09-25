"""Render a portfolio resume from the supplied Overleaf resume content.

This is a condensed website edition, not a replacement for the Overleaf files.
Requires ReportLab; it is not a dependency of the website itself.
"""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public' if (ROOT / 'public/index.html').is_file() else ROOT
OUT = PUBLIC / 'assets/Weiqi-Wang-Resume.pdf'
FONT_ROOT = Path('/usr/share/fonts/truetype/liberation2')
for name, file in [('Body', 'LiberationSans-Regular.ttf'), ('BodyBold', 'LiberationSans-Bold.ttf'), ('BodyItalic', 'LiberationSans-Italic.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_ROOT / file)))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='BodyBold', italic='BodyItalic', boldItalic='BodyBold')
INK = colors.HexColor('#142647')
BLUE = colors.HexColor('#1d4ed8')
styles = {
    'name': ParagraphStyle('name', fontName='BodyBold', fontSize=20, leading=25, textColor=INK, spaceAfter=5),
    'contact': ParagraphStyle('contact', fontName='Body', fontSize=8, leading=12, textColor=INK, spaceAfter=8),
    'section': ParagraphStyle('section', fontName='BodyBold', fontSize=9, leading=13, textColor=BLUE, spaceBefore=11, spaceAfter=5, keepWithNext=True),
    'role': ParagraphStyle('role', fontName='BodyBold', fontSize=9, leading=13, textColor=INK, spaceBefore=5, spaceAfter=4, keepWithNext=True),
    'body': ParagraphStyle('body', fontName='Body', fontSize=8.1, leading=11.7, textColor=INK, spaceAfter=4),
    'bullet': ParagraphStyle('bullet', fontName='Body', fontSize=8.1, leading=11.7, textColor=INK, leftIndent=10, firstLineIndent=-8, spaceAfter=4),
}
story = []
def p(text, kind='body'):
    story.append(Paragraph(text, styles[kind]))
def bullet(text): p('• ' + text, 'bullet')
def section(text): p(text, 'section')
def role(text): p(text, 'role')

p('Weiqi (Rocky) Wang', 'name')
p('Robotics Engineer · UCLA Ph.D. Graduate', 'body')
p('<link href="mailto:wwang79@g.ucla.edu">wwang79@g.ucla.edu</link> · 213-952-8007<br/><link href="https://www.linkedin.com/in/weiqiwang93">linkedin.com/in/weiqiwang93</link> · <link href="https://github.com/Rayckey">github.com/Rayckey</link>', 'contact')
section('EDUCATION')
p('<b>University of California, Los Angeles</b> — Ph.D., Mechanical Engineering (Robotics) · September 2026<br/><i>Dissertation: Embodiment-Aware Task Realization for Human–Robot Coexistence</i>')
p('<b>Johns Hopkins University</b> — M.S., Mechanical Engineering (Robotics) · May 2017')
p('<b>University of Miami</b> — B.S., Mechanical Engineering; Minor in Mathematics · May 2015')
section('RESEARCH EXPERIENCE')
role('UCLA · Center for Vision, Cognition, Learning, and Autonomy | Graduate Student Researcher<br/>September 2020–Present')
role('SUN: Agentic Robot Policy Learning with Persistent Task Programs')
bullet('Built Kuafu, an agentic robot-learning harness that turns object videos and language instructions into learned manipulation policies using shared optimal-control and reinforcement-learning objectives.')
bullet('Developed an agent-driven workflow for task decomposition, program verification, diagnosis, and repair, achieving <b>95.6% formation-and-verification success</b> (43/45 runs).')
bullet('Achieved <b>82.03% mean success across nine simulated multi-stage tasks</b> with behavior cloning and residual RL; exceeded evaluated LLM reward-design and zero-shot language-guided planning methods by 69.18 and 72.03 percentage points, respectively.')
bullet('Built a web-based teleoperation application for collecting human demonstrations in simulation with AgileX PIKA task-space controls.')
bullet('Automated successful-demonstration collection at <b>10.57× human teleoperation throughput</b> after training; including controller preparation, broke even at 35 demonstrations on cost and 513 on time per task on average.')
bullet('Trained RGB, point-cloud, and multi-task VLA policies (SmolVLA, WALL-X, π<sub>0.5</sub>). DP3 reached <b>46.02% mean success</b> on nine simulated tasks, 23.6 percentage points above the matched baseline.')
bullet('Developed the DP3 deployment pipeline for <b>zero-shot sim-to-real transfer on Franka FR3 and Kinova Gen3</b> across three robot–gripper configurations, without real-world demonstrations or fine-tuning.')
role('Scene Rearrangement for Human–Robot Co-Activity')
bullet('Led a scene-rearrangement system using hierarchical ASA/CMA-ES optimization, robot footprint and reachability models, learned spatial relationships, and ConceptNet semantics.')
bullet('Improved accessible space by <b>14%</b>, with <b>30% more reachable objects</b> in the published scene evaluation.')
role('Collaborative Motion Planning and Tool Use')
bullet('Contributed to optimization-based mobile manipulation using Virtual Kinematic Chains. Developed trajectory optimization for simulated Baxter tool-use motions and verified the formulation in MATLAB.')

story.append(PageBreak())
p('Weiqi (Rocky) Wang', 'name')
p('Robotics Engineer · <link href="mailto:wwang79@g.ucla.edu">wwang79@g.ucla.edu</link>', 'contact')
section('INDUSTRY EXPERIENCE')
role('OffWorld, Inc. | Software Intern | Pasadena, CA<br/>June–September 2023; June–September 2021')
bullet('Developed a Python computational-geometry simulation framework for prototype autonomous underground mining robots, modeling environmental changes caused by robot sawing actions.')
bullet('Modeled tool-mounted serial-manipulator dynamics and enabled task-specific force-feedback control. Developed sampling- and optimization-based dual-arm motion planning, with 100% planning success in the evaluated scenarios.')
bullet('Built ROS/ROS 2, Gazebo, and RViz testbeds for multi-robot coordination and navigation, and procedurally generated Webots scenarios for varied test conditions.')
role('CloudMinds / INNFOS Technology Ltd. | Algorithm Engineer | Beijing, China<br/>December 2017–September 2019')
bullet('Led development and maintenance of ROS control software in C++ for the XR1 dual-arm mobile humanoid. Implemented wearable-IMU teleoperation of a 34-degree-of-freedom robot.')
bullet('Developed dynamic parameter identification for mobile dual-arm robots; applied the models to dynamic compensation, collision detection, and impedance/admittance control.')
bullet('Tuned position, velocity, and current control loops for joint actuators. Engineered quadruped walking and trotting control in C++ with six-degree-of-freedom body-pose regulation.')
section('EARLIER RESEARCH &amp; TEACHING')
role('Johns Hopkins University · Laboratory for Computational Sensing + Robotics<br/>Research Assistant | June 2016–September 2017')
bullet('Evaluated fiber Bragg grating shape sensors; built a MATLAB interface for real-time needle reconstruction and integrated low-level control. Contributed to optimal-control virtual fixtures for collaborative ultrasound imaging.')
bullet('Led a haptic femur-drilling simulator in CHAI3D, integrating CT-derived anatomical models and haptic feedback. Implemented model-based gravity compensation for the da Vinci Research Kit master arm.')
p('<b>UCLA · Instructor &amp; Teaching Fellow, Mathematics for Life Scientists</b> — 6 years; nominated for the Distinguished Teaching Award for Teaching Assistants.')
section('TECHNICAL SKILLS')
p('<b>Languages &amp; tools:</b> Python, C++, MATLAB, PyTorch, ROS/ROS 2, CasADi, Linux, Git, SolidWorks.<br/><b>Learning:</b> Imitation learning, behavior cloning, residual RL, visuomotor policies, VLA training, sim-to-real.<br/><b>Planning &amp; control:</b> MPC, trajectory optimization, sampling-based planning, robot dynamics, system identification, impedance/admittance control, teleoperation.<br/><b>Perception:</b> 6D pose estimation, state estimation, sensor fusion, point-cloud registration, RGB-D calibration.<br/><b>Simulation &amp; hardware:</b> Isaac Lab/Sim, MuJoCo, PyBullet, Gazebo, Webots, CoppeliaSim, CAN bus, UR5, Franka FR3, Kinova Gen3.')
section('SELECTED PUBLICATIONS')
p('<b>Wang, W.</b>, et al. “SUN: Agentic Robot Policy Learning with Persistent Task Programs.” <i>Under Review</i>, 2026.<br/><b>Wang, W.</b>, et al. “Rearrange Indoor Scenes for Human–Robot Co-Activity.” <i>IEEE ICRA</i>, 2023.<br/>Zhang, Z., et al. “Understanding Physical Effects for Effective Tool-Use.” <i>IEEE RA-L</i>, 2022.<br/>Jiao, Z., et al. “Efficient Task Planning for Mobile Manipulation: A Virtual Kinematic Chain Perspective.” <i>IEEE/RSJ IROS</i>, 2021.<br/>Zahedi, E., et al. “Towards Skill Transfer via Learning-Based Guidance in Human–Robot Interaction: An Application to Orthopaedic Surgical Drilling Skill.” <i>Journal of Intelligent &amp; Robotic Systems</i>, 2020.')

def footer(canvas, doc):
    canvas.setFont('Body', 7)
    canvas.setFillColor(colors.HexColor('#526884'))
    canvas.drawRightString(letter[0] - 42, 25, str(doc.page))

if __name__ == '__main__':
    doc = SimpleDocTemplate(str(OUT), pagesize=letter, rightMargin=42, leftMargin=42, topMargin=34, bottomMargin=35, title='Weiqi (Rocky) Wang — Robotics Resume', author='Weiqi Wang')
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print('Built', OUT)
