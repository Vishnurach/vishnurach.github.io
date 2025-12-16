import os

# ==========================================
# 1. DATA ENTRY
# ==========================================
workshop_data = [
    {
        "title": "Workshop on Arduino Programming & Hardware Interface",
        "role": "Resource Person",
        "date": "Feb 21 – 22, 2022",
        "venue": "Vidya Academy of Science and Technology (EEE Dept)",
        "audience": "Students from Thiagarajar Polytechnic College, Alagappanagar",
        "description": [
            "Led a two-day hands-on workshop on Arduino IDE and Tinkercad simulation.",
            "Trained students on digital/analog I/O, sensor interfacing, LCD displays, and serial monitoring.",
            "Guided students in completing a final hardware project integrating these concepts."
        ],
        "images": ["workshop_1.jpg", "workshop_2.jpg", "workshop_3.jpg", "workshop_4.jpg"]
    },
    {
        "title": "Workshop on Arduino Programming and LED Bulb Assembly",
        "role": "Resource Person",
        "date": "Dec 17 – 18, 2018",
        "venue": "Vidya Academy of Science and Technology (EEE Dept)",
        "audience": "Students from Polytechnic Colleges in Kerala",
        "description": [
            "Hosted a two-day workshop focused on Arduino programming, interfacing, and applications.",
            "Conducted a half-day hands-on session on LED bulb assembling and testing.",
            "Covered topics including Analog/Digital I/O, Actuator control, and Control of indicating devices."
        ],
        "images": ["workshop_2_1.jpg", "workshop_2_2.jpg"]
    },
    {
        "title": "Project Based Learning (PBL) & Product Development",
        "role": "Project Supervisor",
        "date": "March 2022",
        "venue": "Vidya Academy of Science & Technology (EEE Dept)",
        "audience": "S3 B.Tech EEE Students",
        "description": [
            "Implemented Student-Centered Learning via Project Based Learning (PBL) for third-semester students.",
            "Supervised students in developing electronic hardware products as part of the subject Design and Engineering.",
            "Guided students through product demonstration with PowerPoint presentations and technical reports."
        ],
        "images": ["pbl_landscape_1.jpg", "pbl_landscape_2.jpg"],
        "gallery_col": "1fr" 
    },
    {
        "title": "Workshop on Household Equipment Servicing",
        "role": "Resource Person",
        "date": "Nov 27, 2021",
        "venue": "Government Women's Polytechnic College, Nedupuzha",
        "audience": "Students of Government Women's Polytechnic College",
        "description": [
            "Organized as part of the Innovators' Premier League (IPL) initiative by Kerala Start-up Mission (KSUM).",
            "Demonstrated servicing of ceiling fans, exhaust fans, iron boxes, grinders, vacuum cleaners, and electric kettles.",
            "Collaborated with student co-resource person to facilitate practical sessions."
        ],
        "images": ["workshop_3_1.jpg", "workshop_3_2.jpg", "workshop_3_3.jpg", "workshop_3_4.jpg"]
    },
    {
        "title": "Expert Interaction Classes on Energy Conservation",
        "role": "Resource Person",
        "date": "Feb 24 – Mar 4, 2022",
        "venue": "Online (Various Vocational Higher Secondary Schools in Kerala)",
        "audience": "Students from Edamon, Kunnamkulam, Vallakkadavu, Sreekandeswaram, and Vadakkadathukavu VHSS",
        "description": [
            "Conducted a series of online interactive sessions on 'Home Energy Conservation' for VHSS students.",
            "Organized by the Industry Institute Interaction Cell (IIIC), Department of General Education, Govt. of Kerala.",
            "Focused on energy-efficient appliances, home energy assessment, and best practices for domestic electrical solutions."
        ],
        "images": ["workshop_4_1.jpg", "workshop_4_2.jpg", "workshop_4_3.jpg", "workshop_4_4.jpg", "workshop_4_5.jpg"],
        "fit": "contain",
        "gallery_col": "1fr 1fr 1fr" 
    }
]

achievement_data = [
    {
        "title": "First Position - AAC Device Development Challenge",
        "organizer": "NISH & APJ Abdul Kalam Technological University (KTU)",
        "date": "July 2022",
        "role": "System Architect",
        "description": [
            "Secured 1st Prize in the state-level challenge organized by NISH (National Institute of Speech and Hearing) and KTU.",
            "Designed and validated schematics and 2-layer PCB layouts, covering full component selection.",
            "The award was distributed by Hon. Higher Education Minister of Kerala, Dr. R. Bindu."
        ],
        "images": ["achievement_1.jpg", "achievement_2.jpg", "news_1.jpg", "news_2.jpg"],
        "gallery_col": "1fr 1fr"
    },
    {
        "title": "Outstanding Contribution Award",
        "organizer": "BTL India Pvt Ltd (Medical Division)",
        "date": "Dec 2024",
        "role": "R&D Engineer",
        "layout": "split", 
        "description": [
            "Awarded for exceptional work and dedication on the Holter ECG medical device development project.",
            "Developed an automated test system for battery connection reliability, reducing manual testing labor by 90%.",
            "Verified charger IC and battery protection behavior under stress using MCU-based automation and environmental chambers."
        ],
        "images": ["award_holter.jpg"]
    },
    {
        "title": "Empanelled Home Energy Assessor (Top Scorer)",
        "organizer": "Energy Management Centre (EMC) - Kerala",
        "date": "Dec 2021 – Jan 2022",
        "role": "Certified Assessor (Category B)",
        "description": [
            "Empanelled as a Home Energy Assessor by EMC, Government of Kerala, after successfully qualifying the Category B examination.",
            "Secured the top position with a score of 92.5%, standing as the only candidate to surpass the 90% mark in the examination.",
            "Authorized to conduct home energy assessments and act as a consultant for energy-efficient building solutions in Kerala."
        ],
        "pdf": "EMC_Result_Rank_List.pdf", 
        "images": ["EMC_Certificate.jpg"],
        "gallery_col": "1fr"
    }
]

# ==========================================
# 2. HTML GENERATOR FUNCTIONS
# ==========================================
def generate_workshop_html(workshops):
    html_output = ""
    delay_counter = 1
    
    for ws in workshops:
        grid_col = ws.get('gallery_col', '1fr 1fr')
        grid_css = f"grid-template-columns: {grid_col};"
        
        img_style = ""
        
        if grid_col == "1fr":
            img_style = 'style="height: auto; max-height: none; object-fit: contain;"'
        elif ws.get('fit') == 'contain':
            img_style = 'style="object-fit: contain;"'
            grid_css += " gap: 0.75rem;" 
            
        images_html = ""
        for img in ws['images']:
            images_html += f'<img src="{img}" {img_style} alt="Photo" onerror="this.src=\'https://placehold.co/600x400?text=Photo+Placeholder\'">'
            
        desc_html = ""
        for item in ws['description']:
            desc_html += f'<li>{item}</li>'

        html_output += f"""
            <div class="content-block reveal-up delay-{delay_counter}">
                <div class="workshop-header">
                    <h3><i class="fa-solid fa-chalkboard-user"></i> {ws['title']}</h3>
                    <span class="workshop-date"><i class="fa-regular fa-calendar"></i> {ws['date']}</span>
                </div>
                <div class="workshop-meta">
                    <p><strong>Role:</strong> {ws['role']} | <strong>Venue:</strong> {ws['venue']}</p>
                    <p style="margin-top:0.5rem;"><strong>Audience:</strong> {ws['audience']}</p>
                </div>
                
                <ul class="project-list" style="margin-top: 1rem;">
                    {desc_html}
                </ul>
                
                <div class="workshop-gallery" style="{grid_css}">
                    {images_html}
                </div>
            </div>
        """
        delay_counter = 1 if delay_counter >= 4 else delay_counter + 1
        
    return html_output

def generate_achievement_html(achievements):
    html_output = ""
    delay_counter = 1
    
    for ach in achievements:
        # Common Data Extraction
        team_info = f" | <strong>Team:</strong> {ach['team']}" if 'team' in ach else ""
        
        # Description Generation
        desc_html = ""
        for item in ach['description']:
            clean_item = item.strip().rstrip('.')
            if clean_item:
                desc_html += f"<li>{clean_item}.</li>"
            
        # PDF Button Logic
        pdf_button_html = ""
        if 'pdf' in ach:
            pdf_button_html = f"""
            <div style="margin-top: 1.5rem;">
                <a href="{ach['pdf']}" target="_blank" class="pdf-btn">
                    <i class="fa-solid fa-file-pdf"></i> View Result Rank List (PDF)
                </a>
            </div>
            """

        # Layout Decision
        layout = ach.get('layout', 'normal')
        
        if layout == 'split':
            # Split Layout: Text Left, Image Right
            images_html = ""
            for img in ach['images']:
                images_html += f'<img src="{img}" class="split-img" alt="Achievement Photo" onerror="this.src=\'https://placehold.co/600x400?text=Achievement+Photo\'">'

            html_output += f"""
            <div class="content-block reveal-up delay-{delay_counter}">
                <div class="split-layout">
                    <div class="split-content">
                        <div class="workshop-header">
                            <h3><i class="fa-solid fa-trophy"></i> {ach['title']}</h3>
                            <span class="workshop-date"><i class="fa-regular fa-calendar"></i> {ach['date']}</span>
                        </div>
                        <div class="workshop-meta">
                            <p><strong>Organized By:</strong> {ach['organizer']}</p>
                            <p style="margin-top:0.5rem;"><strong>Role:</strong> {ach['role']}{team_info}</p>
                        </div>
                        <ul class="project-list" style="margin-top: 1rem;">
                            {desc_html}
                        </ul>
                        {pdf_button_html}
                    </div>
                    <div class="split-image-container">
                        {images_html}
                    </div>
                </div>
            </div>
            """
        
        else:
            # Standard Layout: Top to Bottom
            grid_col = ach.get('gallery_col', '1fr 1fr')
            grid_css = f"grid-template-columns: {grid_col};"
            img_style = ""
            if grid_col == "1fr":
                img_style = 'style="height: auto; max-height: 400px; object-fit: contain;"'
            
            images_html = ""
            for img in ach['images']:
                images_html += f'<img src="{img}" {img_style} alt="Achievement Photo" onerror="this.src=\'https://placehold.co/600x400?text=Achievement+Photo\'">'

            html_output += f"""
                <div class="content-block reveal-up delay-{delay_counter}">
                    <div class="workshop-header">
                        <h3><i class="fa-solid fa-trophy"></i> {ach['title']}</h3>
                        <span class="workshop-date"><i class="fa-regular fa-calendar"></i> {ach['date']}</span>
                    </div>
                    <div class="workshop-meta">
                        <p><strong>Organized By:</strong> {ach['organizer']}</p>
                        <p style="margin-top:0.5rem;"><strong>Role:</strong> {ach['role']}{team_info}</p>
                    </div>
                    
                    <ul class="project-list" style="margin-top: 1rem;">
                        {desc_html}
                    </ul>
                    
                    {pdf_button_html}
                    
                    <div class="workshop-gallery" style="{grid_css}">
                        {images_html}
                    </div>
                </div>
            """
            
        delay_counter = 1 if delay_counter >= 4 else delay_counter + 1
        
    return html_output

workshops_section_content = generate_workshop_html(workshop_data)
achievements_section_content = generate_achievement_html(achievement_data)

# ==========================================
# 3. HELPER: EMAIL OBFUSCATION
# ==========================================
def obfuscate_email(email):
    return "".join([f"&#{ord(c)};" for c in email])

my_email = "vishnurach.official@gmail.com" 
encoded_email = obfuscate_email(my_email)

# ==========================================
# 4. HTML CONTENT TEMPLATE
# ==========================================
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Vishnu Rach K R | Electrical & Electronics Engineer</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Portfolio of Vishnu Rach K R, an Electrical & Electronics Engineer specializing in Firmware, Hardware Design, and Validation.">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

<header class="header">
    <div class="brand-name">
        <i class="fa-solid fa-microchip"></i> Vishnu Rach K R
    </div>
    <nav class="nav" id="navMenu">
        <a href="#home" class="nav-link active"><i class="fa-solid fa-house"></i> Home</a>
        <a href="#skills" class="nav-link"><i class="fa-solid fa-tools"></i> Skills</a>
        <a href="#experience" class="nav-link"><i class="fa-solid fa-briefcase"></i> Experience</a>
        <a href="#projects" class="nav-link"><i class="fa-solid fa-project-diagram"></i> Projects</a>
        <a href="#achievements-section" class="nav-link"><i class="fa-solid fa-trophy"></i> Achievements</a>
        <a href="#workshops-section" class="nav-link"><i class="fa-solid fa-chalkboard-user"></i> Workshops</a>
        <a href="#contact" class="nav-link"><i class="fa-solid fa-envelope"></i> Contact</a>
    </nav>
    <div class="hamburger" id="hamburger">
        <span></span><span></span><span></span>
    </div>
</header>

<main>

    <section id="home" class="section-home">
        <div class="hero-container">
            <div class="hero-text reveal-left">
                <h1>Electrical & Electronics <br> Engineer</h1>
                <p class="hero-subtitle">
                    <span class="badge"><i class="fa-solid fa-code"></i> Firmware</span> 
                    <span class="badge"><i class="fa-solid fa-microchip"></i> Hardware</span> 
                    <span class="badge"><i class="fa-solid fa-check-double"></i> Validation</span>
                </p>
                <div class="hero-desc">
                    <p>I am a passionate Electrical & Electronics Engineer who loves to tinker, teach, and create. From fixing broken appliances at home to designing complex firmware for industry-leading products, I am driven by a passion for problem-solving. My experience ranges from conducting energy assessments to mentoring the next generation of engineers. When I'm not designing circuits or coding in C, you can find me on the football field, playing cricket, or performing in group dances at cultural events. I bring that same team spirit and energy to every project I undertake.</p>
                </div>
            </div>

            <div class="profile-photo-frame reveal-right">
                <img src="profile.jpg" alt="Vishnu Rach K R" onerror="this.style.display='none'; this.parentElement.classList.add('image-placeholder');">
            </div>
        </div>
    </section>

    <section id="skills" class="section-alt">
        <div class="container">
            <h2 class="section-title reveal-up">Technical Toolbox</h2>
            <div class="skills-grid">
                
                <div class="skill-card reveal-up delay-1">
                    <h3><i class="fa-solid fa-code"></i> Firmware & Embedded</h3>
                    <ul>
                        <li><i class="fa-solid fa-terminal"></i> <strong>Langs:</strong> C, C++, Embedded C, Python</li>
                        <li><i class="fa-solid fa-microchip"></i> <strong>MCUs:</strong> PSoC, PIC, ARM, AVR, ESP8266</li>
                        <li><i class="fa-solid fa-gears"></i> RTOS Fundamentals</li>
                        <li><i class="fa-solid fa-network-wired"></i> I2C, SPI, UART, GPIO, ADC, PWM</li>
                    </ul>
                </div>

                <div class="skill-card reveal-up delay-2">
                    <h3><i class="fa-solid fa-laptop-code"></i> IDEs & Tools</h3>
                    <ul>
                        <li><i class="fa-solid fa-code-branch"></i> PSoC Creator, STM32CubeIDE</li>
                        <li><i class="fa-solid fa-code-branch"></i> Keil μVision, MPLAB X, Arduino IDE</li>
                        <li><i class="fa-solid fa-code-commit"></i> <strong>VCS:</strong> Tortoise SVN</li>
                        <li><i class="fa-solid fa-list-check"></i> <strong>Mgmt:</strong> Jira, Codebeamer</li>
                    </ul>
                </div>

                <div class="skill-card reveal-up delay-3">
                    <h3><i class="fa-solid fa-bezier-curve"></i> Hardware Design (EDA)</h3>
                    <ul>
                        <li><i class="fa-solid fa-layer-group"></i> Altium Designer, KiCad</li>
                        <li><i class="fa-solid fa-wave-square"></i> Proteus, LTSpice (Simulation)</li>
                        <li><i class="fa-solid fa-pen-ruler"></i> Schematic & PCB Design</li>
                        <li><i class="fa-solid fa-check-double"></i> Circuit Analysis</li>
                    </ul>
                </div>
                
                 <div class="skill-card reveal-up delay-4">
                    <h3><i class="fa-solid fa-vial"></i> Testing, Measurement & Automation</h3>
                    <ul>
                        <li><i class="fa-solid fa-chart-line"></i> NI DAQ, MonoDAQ, LabVIEW</li>
                        <li><i class="fa-solid fa-microscope"></i> Oscilloscopes, Logic Analyzers</li>
                        <li><i class="fa-solid fa-plug"></i> Electronic Load, Power Supplies</li>
                        <li><i class="fa-solid fa-car-battery"></i> Battery & Reliability Testing</li>
                    </ul>
                </div>

            </div>
        </div>
    </section>

    <section id="experience" class="section-white">
        <div class="container">
            <h2 class="section-title reveal-up">Professional Journey</h2>
            
            <div class="timeline">
                <div class="timeline-item reveal-up">
                    <div class="timeline-date"><i class="fa-regular fa-calendar-check"></i> Aug 2022 – Jan 2026 (Serving Notice Period)</div>
                    <div class="timeline-content">
                        <h3>R&D Engineer</h3>
                        <span class="company"><i class="fa-solid fa-building"></i> Litin Design Labs / BTL India Pvt Ltd (On Deputation)</span>
                        <ul class="role-list">
                            <li>Developed embedded firmware in C for daughter boards with an MCU and peripheral testing including EEPROM for hardware test jigs.</li>
                            <li>Architected automated validation systems using MCU, MonoDAQ and Dewesoft, reducing manual test time by 40%.</li>
                            <li>Designed circuits and managed component selection using Altium and LTSpice.</li>
                            <li>Executed comprehensive hardware test plans at board and system levels.</li>
                        </ul>
                    </div>
                </div>

                <div class="timeline-item reveal-up">
                    <div class="timeline-date"><i class="fa-regular fa-calendar"></i> Jan 2016 – Aug 2022</div>
                    <div class="timeline-content">
                        <h3>Assistant Professor cum Research Assistant</h3>
                        <span class="company"><i class="fa-solid fa-university"></i> Vidya Academy of Science and Technology</span>
                        <ul class="role-list">
                            <li>Architected the complete system for an award-winning AAC (Augmentative and Alternative Communication) device.</li>
                            <li>Instructed 100+ students in embedded firmware development and hardware design.</li>
                            <li>Developed laboratory curricula for microcontroller applications.</li>
                        </ul>
                    </div>
                </div>

                <div class="timeline-item reveal-up">
                    <div class="timeline-date"><i class="fa-regular fa-calendar"></i> Jul 2019 – Dec 2019</div>
                    <div class="timeline-content">
                        <h3>Senior Research Fellow (Sabbatical)</h3>
                        <span class="company"><i class="fa-solid fa-flask"></i> Indian Institute of Technology (IIT), Delhi</span>
                        <ul class="role-list">
                            <li>Built NI DAQ + LabVIEW setups to monitor battery State of Charge (SoC).</li>
                            <li>Implemented Arduino/MATLAB control for battery charge/discharge testing.</li>
                            <li>Authored coding tutorials for STM32 microcontrollers.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="projects" class="section-alt">
        <div class="container">
            <h2 class="section-title reveal-up">Featured Projects</h2>
            
            <div class="projects-grid">
                <article class="project-card reveal-up delay-1">
                    <div class="project-header">
                        <h3><i class="fa-solid fa-pump-medical"></i> Infusion Pump</h3>
                        <div class="tags">
                            <span>PSoC</span><span>Altium</span><span>IEC 60601</span>
                        </div>
                    </div>
                    <div class="project-body">
                        <ul class="project-list">
                            <li>Developed firmware in PSoC Creator to validate daughter board integration.</li>
                            <li>Developed firmware to control automated PCBA testing via custom test jig.</li>
                            <li>Designed a BMS and power architecture in Altium, validating circuits in LTSpice to ensure patient safety standards.</li>
                        </ul>
                    </div>
                </article>

                <article class="project-card reveal-up delay-2">
                    <div class="project-header">
                        <h3><i class="fa-solid fa-heart-pulse"></i> Holter ECG Machine</h3>
                        <div class="tags">
                            <span>Automation</span><span>Li-ion</span><span>Testing</span>
                        </div>
                    </div>
                    <div class="project-body">
                        <ul class="project-list">
                            <li>Developed an automated test system for battery connection reliability, eliminating 90% of manual testing labor.</li>
                            <li>Verified charger IC and battery pack protection behavior under environmental stress conditions using MCU based automated system and environmental chamber.</li>
                        </ul>
                    </div>
                </article>

                <article class="project-card reveal-up delay-3">
                    <div class="project-header">
                        <h3><i class="fa-solid fa-microchip"></i> Invasive Cardiology Board</h3>
                        <div class="tags">
                            <span>ARM</span><span>Ethernet</span><span>Hardware Design</span>
                        </div>
                    </div>
                    <div class="project-body">
                        <ul class="project-list">
                            <li>Designed schematics for a carrier board featuring power supplies, ARM microcontroller, and communication peripherals (Ethernet, SPI, USB-UART, RS485, OFC) in Altium Designer.</li>
                            <li>Executed hardware evaluation plans and system level noise performance test.</li>
                        </ul>
                    </div>
                </article>

                <article class="project-card reveal-up delay-4">
                    <div class="project-header">
                        <h3><i class="fa-solid fa-comments"></i> AAC Device (Award Winner)</h3>
                        <div class="tags">
                            <span>Product Design</span><span>System Architecture</span>
                        </div>
                    </div>
                    <div class="project-body">
                        <ul class="project-list">
                            <li>Designed the complete system for an Augmentative and Alternative Communication device for NISH (National Institute of Speech and Hearing).</li>
                            <li>Won First Place in a State-Wide Competition (July 2022).</li>
                        </ul>
                    </div>
                </article>
            </div>
        </div>
    </section>

    <section id="achievements-section" class="section-white">
        <div class="container">
            <h2 class="section-title reveal-up">Key Achievements</h2>
            {achievements_section_content}
        </div>
    </section>

    <section id="workshops-section" class="section-alt">
        <div class="container">
            <h2 class="section-title reveal-up">Workshops & Mentorship</h2>
            {workshops_section_content}
        </div>
    </section>

    <section id="contact" class="section-white">
        <div class="container contact-container">
            <h2 class="section-title reveal-up">Get In Touch</h2>
            <p class="contact-intro reveal-up">
                I am currently serving my notice period and available for immediate opportunities in Embedded Systems.
            </p>
            
            <div class="contact-links">
                <a href="mailto:{encoded_email}" class="contact-card reveal-up delay-1">
                    <i class="fa-solid fa-at"></i>
                    <h3>Email Me</h3>
                    <p>{encoded_email}</p>
                </a>
                
                <a href="https://linkedin.com/in/vishnurachkr" target="_blank" class="contact-card reveal-up delay-2">
                    <i class="fa-brands fa-linkedin"></i>
                    <h3>LinkedIn</h3>
                    <p>linkedin.com/in/vishnurachkr</p>
                </a>
            </div>
        </div>
    </section>

</main>

<footer class="footer">
    <p>&copy; 2025 Vishnu Rach K R. All Rights Reserved.</p>
</footer>

<script src="js/script.js"></script>
</body>
</html>
"""

# ==========================================
# 5. CSS CONTENT
# ==========================================
css_content = """/* Variables */
:root {
    --primary: #2563eb;
    --secondary: #1e293b;
    --accent: #3b82f6;
    --bg-white: #ffffff;
    --bg-alt: #f1f5f9;
    --text-dark: #1e293b;
    --text-light: #475569;
    --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --hover-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    font-family: 'Inter', sans-serif;
    color: var(--text-dark);
    line-height: 1.6;
    overflow-x: hidden;
}

h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif;
    color: var(--secondary);
}

a { text-decoration: none; color: inherit; }

/* Navigation */
.header {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 5%;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    z-index: 1000;
}

.brand-name {
    font-weight: 700;
    font-size: 1.25rem;
    color: var(--primary);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.nav { display: flex; gap: 2rem; }

.nav-link {
    font-weight: 500;
    color: var(--text-dark);
    transition: color 0.3s;
    font-size: 0.95rem;
    position: relative;
}

.nav-link:hover, .nav-link.active { color: var(--primary); }

.nav-link::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: -5px;
    left: 0;
    background-color: var(--primary);
    transition: width 0.3s;
}

.nav-link.active::after { width: 100%; }
.nav-link i { margin-right: 5px; }

/* Hamburger */
.hamburger { display: none; cursor: pointer; }
.hamburger span {
    display: block; width: 25px; height: 3px;
    background: var(--text-dark); margin: 5px 0;
    transition: 0.3s;
}

/* Sections */
section {
    padding: 5rem 2rem;
    min-height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.section-home { background: var(--bg-white); padding-top: 8rem; }
.section-white { background: var(--bg-white); }
.section-alt { background: var(--bg-alt); }

.container {
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
}

.section-title {
    font-size: 2rem;
    margin-bottom: 3rem;
    text-align: center;
    position: relative;
    padding-bottom: 1rem;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 4px;
    background: var(--primary);
    border-radius: 2px;
}

/* Hero */
.hero-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4rem;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 5%;
}

.hero-text { flex: 1; max-width: 600px; }
.hero-text h1 {
    font-size: 3.5rem;
    line-height: 1.1;
    margin-bottom: 1rem;
    background: linear-gradient(to right, var(--secondary), var(--primary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-subtitle { display: flex; gap: 1rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
.badge {
    background: #e0e7ff; color: var(--primary);
    padding: 0.4rem 0.8rem; border-radius: 20px;
    font-weight: 600; font-size: 0.9rem;
    display: flex; align-items: center; gap: 0.5rem;
}
.hero-desc { font-size: 1.15rem; color: var(--text-light); margin-bottom: 2rem; text-align: justify; }

.profile-photo-frame {
    position: relative;
    width: 350px;
    height: 350px;
}
.profile-photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 20px;
    box-shadow: 20px 20px 0 var(--primary);
    transition: transform 0.3s;
}
.image-placeholder::before {
    content: 'Photo Not Found (Add profile.jpg)';
    position: absolute; top: 0; left: 0;
    width: 350px; height: 350px;
    background: #e2e8f0; border-radius: 20px;
    box-shadow: 20px 20px 0 var(--primary);
    display: flex; align-items: center; justify-content: center;
    color: var(--text-light); font-weight: 600;
    text-align: center; border: 2px dashed #cbd5e1;
}

/* Skills Grid */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
}
.skill-card {
    background: white; padding: 2rem; border-radius: 12px;
    box-shadow: var(--card-shadow); transition: transform 0.3s;
    border-top: 4px solid var(--primary);
}
.skill-card:hover { transform: translateY(-5px); box-shadow: var(--hover-shadow); }
.skill-card h3 { margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }
.skill-card ul { list-style: none; }
.skill-card li { margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.8rem; color: var(--text-light); font-size: 0.95rem; }
.skill-card li i { color: var(--accent); width: 20px; flex-shrink: 0; }

/* Timeline */
.timeline { position: relative; max-width: 800px; margin: 0 auto; }
.timeline::before {
    content: ''; position: absolute; left: 20px; top: 0; bottom: 0; width: 2px; background: #cbd5e1;
}
.timeline-item { position: relative; padding-left: 60px; margin-bottom: 3rem; }
.timeline-item::before {
    content: ''; position: absolute; left: 11px; top: 24px;
    width: 20px; height: 20px; background: var(--primary);
    border: 4px solid #fff; border-radius: 50%; box-shadow: 0 0 0 2px var(--primary);
}
.timeline-date {
    font-size: 0.9rem; font-weight: 600; color: var(--primary);
    margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;
}
.timeline-content {
    background: white; padding: 1.5rem; border-radius: 12px;
    box-shadow: var(--card-shadow); border: 1px solid #f1f5f9;
}
.company { display: block; font-weight: 600; color: var(--text-light); margin-bottom: 1rem; }
.role-list { margin-left: 1.5rem; margin-top: 1rem; color: var(--text-light); }

/* Projects */
.projects-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;
}
.project-card {
    background: white; border-radius: 12px; overflow: hidden;
    box-shadow: var(--card-shadow); transition: transform 0.3s;
    display: flex; flex-direction: column;
}
.project-card:hover { transform: translateY(-5px); box-shadow: var(--hover-shadow); }
.project-header { background: var(--secondary); color: white; padding: 1.5rem; }
.project-header h3 { color: white; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem; }
.tags { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.5rem; }
.tags span { background: rgba(255,255,255,0.2); padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.8rem; }
.project-body { padding: 1.5rem; color: var(--text-light); flex: 1; }
.project-list { margin-left: 1.5rem; list-style-type: disc; }
.project-list li { margin-bottom: 0.5rem; color: var(--text-light); font-size: 0.95rem; }

/* Workshops & Mentorship (Reused for Achievements) */
.content-block {
    background: white; padding: 2rem; margin-bottom: 1.5rem;
    border-radius: 12px; box-shadow: var(--card-shadow);
    max-width: 900px; margin-left: auto; margin-right: auto;
    border-left: 5px solid var(--primary);
}
.workshop-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 0.5rem; }
.workshop-header h3 { margin-bottom: 0; font-size: 1.25rem; color: var(--primary); }
.workshop-date { background: #e0e7ff; color: var(--primary); padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: 600; font-size: 0.9rem; }
.workshop-meta { color: var(--text-dark); margin-bottom: 1rem; font-size: 0.95rem; }
.workshop-gallery { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1.5rem; }
.workshop-gallery img { width: 100%; height: 250px; object-fit: cover; border-radius: 8px; transition: transform 0.3s; cursor: pointer; }
.workshop-gallery img:hover { transform: scale(1.02); }

/* Split Layout for Achievements */
.split-layout {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 2rem;
    align-items: center;
}
.split-content {
    display: flex;
    flex-direction: column;
}

/* Image Container to center the trophy */
.split-image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}

.split-img {
    width: auto;
    max-width: 100%;
    height: auto;
    max-height: 450px; /* Increased height for vertical trophy */
    object-fit: contain; /* Ensure full trophy is visible */
    border-radius: 8px;
    box-shadow: var(--card-shadow);
    transition: transform 0.3s;
}
.split-img:hover { transform: scale(1.02); }

/* PDF Button Styling */
.pdf-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: #ef4444; /* Red color for PDF */
    color: white;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    font-weight: 500;
    font-size: 0.95rem;
    transition: background 0.3s, transform 0.2s;
    text-decoration: none;
    box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);
}
.pdf-btn:hover {
    background: #dc2626;
    transform: translateY(-2px);
    color: white;
}

.training-list { list-style: none; margin-top: 1rem; }
.training-list li { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem; color: var(--text-light); }

/* Contact */
.contact-container { text-align: center; }
.contact-intro { max-width: 600px; margin: 0 auto 3rem; color: var(--text-light); font-size: 1.1rem; }
.contact-links { display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; }
/* UPDATED CONTACT CARD CSS FOR EMAIL OVERFLOW */
.contact-card {
    background: white; padding: 2rem; border-radius: 12px;
    box-shadow: var(--card-shadow);
    width: auto; min-width: 250px; max-width: 350px; /* Allow growth */
    transition: transform 0.3s; text-align: center; color: var(--text-dark);
    word-break: break-word; /* Ensure long emails wrap */
}
.contact-card:hover { transform: translateY(-5px); color: var(--primary); }
.contact-card i { font-size: 2.5rem; margin-bottom: 1rem; color: var(--primary); }
.footer { text-align: center; padding: 2rem; background: var(--secondary); color: white; }

/* ===========================
   SCROLL ANIMATIONS
   =========================== */
.reveal-up { opacity: 0; transform: translateY(50px); transition: all 0.8s ease-out; }
.reveal-left { opacity: 0; transform: translateX(-50px); transition: all 0.8s ease-out; }
.reveal-right { opacity: 0; transform: translateX(50px); transition: all 0.8s ease-out; }
.reveal-visible { opacity: 1; transform: translate(0, 0); }

.delay-1 { transition-delay: 0.1s; }
.delay-2 { transition-delay: 0.2s; }
.delay-3 { transition-delay: 0.3s; }
.delay-4 { transition-delay: 0.4s; }

/* Responsive */
@media (max-width: 768px) {
    .nav {
        position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px);
        background: white; flex-direction: column; align-items: center; padding-top: 2rem;
        transition: 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .nav.active { left: 0; }
    .hamburger { display: block; }
    .hero-container { flex-direction: column-reverse; text-align: center; gap: 2rem; }
    .hero-subtitle { justify-content: center; }
    .profile-photo-frame, .profile-photo-frame img, .image-placeholder::before { width: 280px; height: 280px; }
    .timeline::before { left: 0; }
    .timeline-item { padding-left: 30px; }
    .timeline-item::before { left: -9px; }
    
    /* MOBILE GALLERY FIX: Force 1 column on mobile */
    .workshop-gallery { 
        grid-template-columns: 1fr !important;
    }
    .workshop-gallery img {
        height: auto !important; /* Ensure photos aren't squashed */
        max-height: 400px;
        object-fit: cover;
    }
    
    /* Split Layout Mobile Stack */
    .split-layout {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    .split-img {
        max-height: 350px; /* Reduced height on mobile */
    }
}
"""

# ==========================================
# 6. JAVASCRIPT CONTENT
# ==========================================
js_content = """document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Mobile Menu Toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-link');

    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        hamburger.classList.toggle('toggle');
    });

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            hamburger.classList.remove('toggle'); // Fix: Reset hamburger icon when link is clicked
        });
    });

    // 2. Scroll Animation Observer
    const observerOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');
    revealElements.forEach(el => observer.observe(el));

    // 3. Active Link Highlighter on Scroll
    const sections = document.querySelectorAll('section');
    
    window.addEventListener('scroll', () => {
        let current = '';
        const scrollY = window.scrollY; // Use modern standard over pageYOffset

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= (sectionTop - sectionHeight / 3)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').includes(current)) {
                link.classList.add('active');
            }
        });
    });
});
"""

# ==========================================
# 7. FILE GENERATION
# ==========================================

if not os.path.exists('css'):
    os.makedirs('css')

if not os.path.exists('js'):
    os.makedirs('js')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
    print("Created index.html")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
    print("Created css/style.css")

with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
    print("Created js/script.js")

print("\nSuccess! Website generated.")
