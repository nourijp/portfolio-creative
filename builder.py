import re, os

content = {
    "title": "Hamed Nouri — Creative Direction, Storytelling & Media",
    "description": "Portfolio for creative direction, comics, books, educational media, design, video, audio, and community storytelling by Hamed Nouri.",
    "email": "creative@hamednouri.com",
    "phone": "+1 214 245 0784",
    "hero_h1": "Creative Direction, Storytelling &amp; Media",
    "hero_sub": "I create story-driven projects across comics, books, educational media, design, video, audio, and community platforms.",
    "about": "My creative work spans comic writing and editing, educational product design, community building, multimedia storytelling, and cultural media projects. I combine strategic thinking with hands-on creative production.",
    "location": "Denton, TX",
    "projects": [
        ("MManga — Muslim Creative Community", "Built and managed a Muslim manga and creative community platform with 44K+ audience across social and web platforms."),
        ("Aya &amp; Sura Creative Direction", "Creative direction, writing, and educational design for children's Islamic and Arabic learning products."),
        ("Graphic Novel and Comic Projects", "Writing, editing, and creative direction for Muslim-centered graphic narratives and storytelling projects."),
        ("Educational Media Production", "Creative production for learning videos, audio, illustrations, and instructional materials."),
    ],
    "contact_cta": "Contact creative@hamednouri.com for creative projects, storytelling, or collaboration.",
}

idx = "/Users/hamed/.gemini/antigravity/scratch/portfolio-build-master/sites/creative/index.html"
with open(idx) as f:
    html = f.read()

# Meta tags
html = re.sub(r'<title>[^<]*</title>', f'<title>{content["title"]}</title>', html, flags=re.IGNORECASE)
html = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']*["\']',
              f'<meta name="description" content="{content["description"]}"', html, flags=re.IGNORECASE)
html = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\'][^"\']*["\']',
              f'<meta property="og:title" content="{content["title"]}"', html, flags=re.IGNORECASE)
html = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'][^"\']*["\']',
              f'<meta property="og:description" content="{content["description"]}"', html, flags=re.IGNORECASE)
if 'og:title' not in html:
    og = f'\n    <meta property="og:title" content="{content["title"]}">\n    <meta property="og:description" content="{content["description"]}">\n    <meta property="og:url" content="https://creative.hamednouri.com">'
    html = html.replace('</title>', f'</title>{og}', 1)

# Basic replacements
html = re.sub(r'[Ll]orem ipsum[^<"\']{0,500}', '', html)
for fake in ['Jonathan Doe','Jonathan','Juan Dela Cruz','Juan','John Doe','Your Name',
             'your name','Thomson','Noah','Dominic','Monica','Hudson','Kelly','Minimal',
             'Rabbit Doe','Rabbit','Videograph','Olivia','Kross','Kards','Stisla',
             'Web Designer','Web Developer','UI/UX Designer','Graphic Designer',
             'Frontend Developer','Product Designer','Freelance Designer',
             'Freelancer, Frontend Developer','Freelance']:
    html = re.sub(r'(?<![/\-\._a-z])' + re.escape(fake) + r'(?![/\-\._a-z])', 'Hamed Nouri', html)

html = re.sub(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}(?!\.com/|\.io/|\.org/)',
              content['email'], html)
for placeholder in ['yourname@mail.com','yourname@email.com','mail@example.com',
                    'hello@example.com','contact@example.com','info@example.com']:
    html = html.replace(placeholder, content['email'])

html = re.sub(r'\+1[\s\-\.]?\(?2\d{2}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}', content['phone'], html)
for fake_phone in ['+1234567890','+00 123 456 789','(000) 000-0000','000-000-0000',
                   '+1 555 555 5555','555-555-5555']:
    html = html.replace(fake_phone, content['phone'])

for fake_loc in ['New York, NY','New York, USA','New York','California, USA',
                 'Los Angeles','San Francisco','Somewhere','anywhere']:
    html = html.replace(fake_loc, content['location'])

html = re.sub(r'href=["\']https://bit\.ly/[^"\']*["\']', 'href="https://github.com/nourijp"', html)
html = re.sub(r'href=["\']https://twitter\.com/[a-zA-Z0-9_]+["\']', 'href="https://github.com/nourijp"', html)
html = re.sub(r'href=["\']https://facebook\.com/[a-zA-Z0-9_.]+["\']', 'href="https://github.com/nourijp"', html)
html = re.sub(r'href=["\']https://instagram\.com/[a-zA-Z0-9_.]+["\']', 'href="https://github.com/nourijp"', html)
html = re.sub(r'href=["\']https://dribbble\.com/[^"\']+["\']', 'href="https://github.com/nourijp"', html)
html = re.sub(r'href=["\']https://behance\.net/[^"\']+["\']', 'href="https://github.com/nourijp"', html)

footer_text = f'Hamed Nouri &mdash; portfolio site for selected work in communication, documentation, learning, creative media, systems, and digital projects.'
copyright_text = f'&copy; 2026 Hamed Nouri. All rights reserved.'
html = re.sub(r'Copyright\s*&copy;\s*\d{4}[^<]*', copyright_text + ' ', html)
html = re.sub(r'&copy;\s*\d{4}[^<]{0,80}', copyright_text + ' ', html)

hero = content.get('hero_h1', '')
hero_sub = content.get('hero_sub', '')
if hero:
    for pattern in [
        r'(<h1[^>]*>)(?:(?!Hamed)[^<]|<(?!/h1))*?(</h1>)',
        r'(<h2[^>]*class="[^"]*hero[^"]*"[^>]*>)[^<]*(</h2>)',
    ]:
        m = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
        if m and 'Hamed Nouri' not in m.group():
            html = html[:m.start()] + m.group(1) + hero + m.group(2) + html[m.end():]
            break

FAKE_PHRASES = [
    ("I must explain to you how all this mistaken idea", "I work across communication, documentation, learning, creative media, and technical systems."),
    ("Far far away, behind the word mountains", ""),
    ("The copy warned the Little Blind Text", ""),
    ("A small river named Duden", ""),
    ("blind texts", ""),
    ("Vokalia and Consonantia", ""),
    ("Bookmarksgrove", ""),
    ("Separated they live", ""),
    ("in which roasted parts of sentences", ""),
    ("It is a paradisematic country", ""),
    ("regelialia", ""),
    ("paradisematic", ""),
    ("Exercitation culpa qui dolor", ""),
    ("Qui veniam ut consequat ex ullamco", ""),
    ("Do commodo in proident enim", ""),
    ("Occaecat do esse ex et dolor", ""),
    ("Awesome Studio", "CiraConnect"),
    ("Dropbox", "CiraConnect"),
    ("Spotify", "CiraConnect (2021–2024)"),
    ("Google\\nLead UI Designer", "MManga\\nCreative Director"),
    ("Figma\\nUI Designer", "CiraConnect\\nComms & Enablement Lead"),
    ("Microsoft\\nUI Designer", "Self-Directed\\nTechnical Practice"),
    ("Site Of The Month\\nAwwwards — 2023", "MManga\\n44K+ Community Audience"),
    ("Site Of The Day\\nAwwwards — 2023", "CiraConnect Adoption\\n28% Software Adoption Increase"),
    ("Agency of The Year\\nAwwwards — 2022", "Internal Comms Program\\n22% Support Reduction"),
    ("FWA of The Month\\nFWA — 2022", "AI-Assisted Portfolio\\n24 Subdomains Live"),
    ("Site Of The Month\\nAwwwards — 2022", "GIA Practice App\\nSelf-Directed Learning Tool"),
    ("Awwwards", ""),
    ("FWA", ""),
    ("Top Design Trends", "How I Turn Complex Workflows Into Clear Documentation"),
    ("Creative Process", "AI-Assisted Workflows for Writers and Educators"),
    ("Our Work Philosophy", "Building Learning Tools That Actually Work"),
    ("Happy Clients", "Projects Completed"),
    ("Cups of Coffee", "Systems Documented"),
    ("Clue Of The Wooden Cottage", "Aya & Sura Educational Stories"),
    ("Buy Now For $22.78", "Learn More"),
    ("Product Designer", "Communications & Creative Professional"),
    ("UI Designer", "Documentation Specialist"),
    ("Digital Designer", "Systems Specialist"),
]
for old, new in FAKE_PHRASES:
    html = html.replace(old, new)

html = re.sub(
    r'<[^>]*class="[^"]*testimonial[^"]*"[^>]*>.*?(?=<section|</section|<div class="[^"]*section)',
    '<!-- Testimonials removed — no verified testimonials available yet. -->',
    html, flags=re.DOTALL | re.IGNORECASE, count=1
)

html = re.sub(
    r'<[^>]*class="[^"]*team[^"]*"[^>]*>.*?</(?:section|div)>',
    '<!-- Team section removed — solo portfolio. -->',
    html, flags=re.DOTALL | re.IGNORECASE, count=1
)

html = re.sub(
    r'<[^>]*(?:id|class)="[^"]*pric(?:e|ing)[^"]*"[^>]*>.*?</(?:section|div)>',
    '<!-- Pricing section removed. Contact for rates. -->',
    html, flags=re.DOTALL | re.IGNORECASE, count=1
)

html = re.sub(r'Copyright &copy; \d{4}', 'Copyright &copy; 2026 Hamed Nouri.', html)
html = re.sub(r'&copy; \d{4} [A-Za-z ]{2,40}(?=[\.<])', '&copy; 2026 Hamed Nouri', html)

if content.get('about'):
    html = re.sub(
        r'((?:About|about)[^<]{0,30}</h\d>)\s*<p>[^<]{0,600}</p>',
        r'\1\n<p>' + content['about'] + r'</p>',
        html, count=1, flags=re.DOTALL
    )

# Additional manual replacements specific to this template
html = html.replace('VFX / Graphics Head', 'Creative Director & Storyteller')
html = html.replace('12\n              </h2>\n              <p class="text-light-emphasis justify-content-center m-0 ls-4">\n                Years of <br> experience', '12\n              </h2>\n              <p class="text-light-emphasis justify-content-center m-0 ls-4">\n                Years of <br> experience')
html = html.replace('820', '44K+')
html = html.replace('satisfied <br> clients', 'community <br> audience')
html = html.replace('720', '28%')
html = html.replace('employees <br> worldwide', 'adoption <br> increase')
html = html.replace('2200', '22%')
html = html.replace('projects completed', 'support <br> reduction')

html = html.replace('Story &amp; Visual Design', 'Story &amp; Visual Design')
html = html.replace('At in proin consequat ut cursus venenatis sapien.', content['about'][:100] + '...')

html = html.replace('Bachelors in Engineering in Information Technology', 'Creative Direction & Storytelling')
html = html.replace('Harvard School of Science and management', 'Hamed Nouri')

html = html.replace('Creative Agency Inc.: Design head', 'Creative Community Lead')
html = html.replace('iacentem substantiales um se sed esse haec Possit facis qui a a a patriam .', 'Built and managed a Muslim manga and creative community platform with 44K+ audience.')

html = html.replace('Studio Alpha.: Project Manager', 'Creative Direction, Aya & Sura')
html = html.replace('Dr. Stephen H. King', 'TODO: Reference Name')
html = html.replace('Dr. David Howard', 'TODO: Reference Name')

html = html.replace('Graphic Designing Useful Tips & Best Practices', content['projects'][0][0])
html = html.replace('Best way to do branding of digital products', content['projects'][1][0])
html = html.replace('Top 10 graphic designs review in 2022', content['projects'][2][0])

html = html.replace('As a passionate life coach and entrepreneur, I\'m dedicated to guiding you on your journey to success and\n                fulfillment.', content['hero_sub'])
html = html.replace('Leave a Message', 'Get in Touch')
html = html.replace('Labore accusam in modo compungi, iacentem substantiales um se sed esse haec.', content['contact_cta'])
html = html.replace('hamed nouri', 'Your Name')
html = html.replace('your email', 'Your Email')

with open(idx, 'w') as f:
    f.write(html)
