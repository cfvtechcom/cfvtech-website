#!/usr/bin/env python3
"""Generate the static CFV Technologies site (FR at /, EN at /en/) from the original
ASP.NET MVC views. Texts were captured from the live site (cfvtech.com) on 2026-10-15."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "docs"
SITE = "https://cfvtech.com"
LINKEDIN = "https://www.linkedin.com/company/cfvtech/"

T = {
 "fr": dict(
  toggle="Basculer la navigation", home="Accueil", services="Services", certs="Certificats",
  clients="Clients", careers="Carrières", other="EN",
  s1="Préparer et planifier", s2="Concevoir et réaliser", s3="Exploiter et optimiser",
  welcome="Bienvenue chez CFV Technologies",
  welcome_msg="où les <strong>C</strong>lients reçoivent des <strong>F</strong>aits et des <strong>V</strong>aleurs",
  cloud="Infonuagique",
  cloud_msg="Du nuage privé au nuage public, de l'IaaS, du PaaS au SaaS, nous vous aiderons à réduire les coûts, à améliorer la sécurité, à augmenter la flexibilité et encore plus.",
  cyber="La cyber-sécurité",
  cyber_msg="Nos équipes sont spécialisées dans l'amélioration de la sécurité de l'infrastructure aux applications, de l'évaluation des risques aux tests, de la gouvernance aux opérations de sécurité et encore plus.",
  network="Réseau",
  network_msg="Plus que jamais, le réseau doit être transformé pour permettre les affaires dans un monde en évolution rapide. Faites en sorte que le \"Software-defined network\" se produise partout : du LAN au WAN, du réseau câblé au réseau sans fil et encore plus.",
  join_msg="Le succès de nos clients ne peut être atteint sans le succès de nos employés, c'est pourquoi nous motivons toujours l'apprentissage tout au long de la vie dans un monde en évolution rapide et les certifications montrent une partie de nos motivations.",
  join="Rejoignez nos équipes",
  reference="Référence",
  reference_msg="Nous ne pouvons réussir sans le succès de nos clients, c'est pourquoi les clients font confiance à nos services dans différentes missions critiques.",
  work="Travailler avec nous",
  work_msg="Le succès de nos clients ne peut être atteint sans le succès de nos employés. Nous pensons que chaque candidat est unique et que nos projets avec nos clients sont en constante évolution, {li}contactez-nous sur LinkedIn{/li} pour plus de détails. Votre futur emploi n'est qu'à un clic.",
  positions="Postes", positions_msg="Nous sommes constamment à la recherche de talents dans différents domaines.",
  architect="Architecte", autoeng="Ingénieur en automatisation", analyst="Analyste", admin="Administrateur",
  cloudsec="Sécurité infonuagique", risk="Gestion des risques", incident="La gestion des incidents",
  operation="Opération", governance="Gouvernance", pentest="Pentest", appsec="Sécurité des applications",
  netsec="Sécurité Internet", projcs="Projet &amp; Service client", pm="Chef de projet",
  am="Gestionnaire de compte", care="Service client",
  desc="CFV Technologies – services-conseils en infonuagique, cyber-sécurité et réseau.",
  careers_title="Carrières",
 ),
 "en": dict(
  toggle="Toggle navigation", home="Home", services="Services", certs="Certifications",
  clients="Clients", careers="Careers", other="FR",
  s1="Prepare and Planning", s2="Design and Implement", s3="Operate and Optimize",
  welcome="Welcome To CFV Technologies",
  welcome_msg="where <strong>C</strong>ustomers are provided with <strong>F</strong>acts and <strong>V</strong>alues",
  cloud="Cloud Computing",
  cloud_msg="From private cloud to public cloud, from IaaS, PaaS, to SaaS, we will help you with Cost savings, Security improvements, increase in Flexibility and more.",
  cyber="Cyber Security",
  cyber_msg="Our teams are specialized with improving security from infrastructure to applications, from risk assessment to testing, from governance to security operation and more.",
  network="Network",
  network_msg="More than ever network needs to be transformed to enable business in a quickly changing world. Let make software defined network happen everywhere: from LAN to WAN, from wired to wireless network and more.",
  join_msg="Success of our customers can not be achieved without the success of our employees, that's why we always motivate lifelong learning in a rapidly changing world and certifications show a part of our motivations.",
  join="Join our teams",
  reference="Reference",
  reference_msg="We cannot succeed without the success of our customers, that is why customers trust our services in different critical missions.",
  work="Work with us",
  work_msg="Success of our customers can not be achieved without the success of our employees. We believe that every candidate is unique and our projects with customers are constantly evolving, {li}contact us on LinkedIn{/li} for more details. Your future job is only one click away.",
  positions="Positions", positions_msg="We are constantly looking for talent in different domains.",
  architect="Architect", autoeng="Automation Engineer", analyst="Analyst", admin="Administrator",
  cloudsec="Cloud Security", risk="Risk Management", incident="Incident Management",
  operation="Operation", governance="Governance", pentest="Pentest", appsec="Application Security",
  netsec="Network Security", projcs="Project &amp; Customer services", pm="Project Manager",
  am="Account Manager", care="Customer Care",
  desc="CFV Technologies – cloud computing, cyber security and network consulting.",
  careers_title="Careers",
 ),
}

# page paths relative to site root
PATHS = {("fr", "home"): "index.html", ("fr", "careers"): "carrieres.html",
         ("en", "home"): "en/index.html", ("en", "careers"): "en/careers.html"}


def url(lang, page):
    p = PATHS[(lang, page)]
    return "/" + p.replace("index.html", "")


def layout(lang, page, body):
    t = T[lang]
    other = "en" if lang == "fr" else "fr"
    r = "../" if lang == "en" else ""          # relative path back to the site root
    title = "CFV Technologies" if page == "home" else f"{t['careers_title']} – CFV Technologies"
    careers_file = PATHS[(lang, "careers")].split("/")[-1]
    # explicit file names (not "./") so links also work when the files are opened straight from a folder
    other_href = r + ("" if other == "fr" else "en/") + PATHS[(other, page)].split("/")[-1]
    def nav(anchor):
        return f"#{anchor}" if page == "home" else f"index.html#{anchor}"
    alt = "\n".join(
        f'    <link rel="alternate" hreflang="{l}" href="{SITE}{url(l, page)}">' for l in ("fr", "en"))
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="format-detection" content="telephone=no">
    <meta name="description" content="{t['desc']}">
    <title>{title}</title>
    <link rel="canonical" href="{SITE}{url(lang, page)}">
{alt}
    <link rel="icon" href="{r}assets/images/logo.ico" type="image/x-icon">
    <link href="https://fonts.googleapis.com/css?family=Roboto|Open+Sans&amp;display=swap" rel="stylesheet">
    <link href="{r}assets/css/reset.css" rel="stylesheet">
    <link href="{r}assets/css/font-awesome.css" rel="stylesheet">
    <link href="{r}assets/css/bootstrap.css" rel="stylesheet">
    <link href="{r}assets/css/slick.css" rel="stylesheet">
    <link href="{r}assets/css/theme-color/default-theme.css" rel="stylesheet">
    <link href="{r}assets/css/styles.css" rel="stylesheet">
    <link href="{r}assets/css/static.css" rel="stylesheet">
</head>
<body class="page">
    <a class="scrollToTop" href="#"><i class="fa fa-angle-up"></i></a>
    <header id="mu-header">
        <div class="container">
            <nav class="navbar navbar-default mu-main-navbar" role="navigation">
                <div class="navbar-header">
                    <a class="navbar-brand" href="index.html"><img src="{r}assets/images/logo-1.jpg" alt="CFV Technologies"></a>
                    <div class="navbar-btn">
                        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                            <span class="sr-only">{t['toggle']}</span>
                            <span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span>
                        </button>
                    </div>
                </div>
                <div id="navbar" class="navbar-collapse collapse">
                    <ul id="top-menu" class="nav navbar-nav navbar-right mu-main-nav">
                        <li><a href="index.html">{t['home']}</a></li>
                        <li><a href="{nav('mu-services')}">{t['services']}</a></li>
                        <li><a href="{nav('mu-certifications')}">{t['certs']}</a></li>
                        <li><a href="{nav('mu-reference')}">{t['clients']}</a></li>
                        <li><a href="{careers_file}">{t['careers']}</a></li>
                        <li><button class="btn-cfv btn-lang"><a href="{other_href}" hreflang="{other}" lang="{other}">{t['other']}</a></button></li>
                    </ul>
                </div>
            </nav>
        </div>
    </header>
{body}
    <div id="mu-copyright">
        <div class="container">
            <div class="copyright">
                <div class="copyright-term">
                    <p class="footer--text">Copyright &copy; <a href="https://cfvtech.com" class="footer--text web__link">cfvtech.com</a> | All right reserved</p>
                    <p class="footer--text">Developed by VGK Solutions</p>
                    <p class="footer--text">Graphic Design by NTT</p>
                </div>
            </div>
        </div>
    </div>

    <script src="{r}assets/js/jquery.min.js"></script>
    <script src="{r}assets/js/bootstrap.js"></script>
    <script src="{r}assets/js/slick.js"></script>
    <script src="{r}assets/js/site.js"></script>
</body>
</html>
"""


def carousel(lang, images, alt):
    r = "../" if lang == "en" else ""
    items = "\n".join(
        f"""                    <li><div class="mu-single-chef"><figure class="mu-single-chef-img"><img src="{r}assets/images/{img}" alt="{a}"></figure></div></li>"""
        for img, a in zip(images, alt))
    return f"""    <div class="animation-content">
        <div class="container">
            <div class="mu-chef-content">
                <ul class="mu-chef-nav">
{items}
                </ul>
            </div>
        </div>
    </div>"""


CERTS = [f"cert-{i}.png" for i in range(1, 10)]
CLIENTS = ["telus.png", "bell.png", "domtar.png", "exfo.png", "rio.png", "attindas.png",
           "Agropur.png", "Cirque.png", "IA_F.png"]
CLIENT_NAMES = ["TELUS", "Bell", "Domtar", "EXFO", "Rio Tinto", "Attindas Hygiene Partners", "Agropur",
                "Cirque du Soleil", "iA Financial Group"]


def home(lang):
    t = T[lang]; r = "../" if lang == "en" else ""
    careers_file = PATHS[(lang, "careers")].split("/")[-1]
    def slide(img, txt):
        return f"""            <div class="mu-top-slider-single">
                <img src="{r}assets/images/{img}" alt="">
                <div class="mu-top-slider-content"><span class="mu-slider-small-title">{txt}</span></div>
            </div>"""
    def service(img, h, msg):
        return f"""                <div class="service-column">
                    <div class="service-icon"><img src="{r}assets/images/{img}" alt=""></div>
                    <div class="column-heading"><h3>{h}</h3></div>
                    <div class="service-text"><p>{msg}</p></div>
                </div>"""
    return f"""    <section id="mu-slider">
        <div class="mu-slider-area">
        <div class="mu-top-slider">
{slide('slider-1-1.png', t['s1'])}
{slide('slider-2-2.png', t['s2'])}
{slide('slider-3-3.png', t['s3'])}
        </div>
        </div>
    </section>

    <div id="mu-services">
        <div class="container">
        <div class="services-content">
            <div class="welcome-content">
                <h2>{t['welcome']}</h2>
                <p>{t['welcome_msg']}</p>
            </div>
            <div class="service-container">
{service('cloud.png', t['cloud'], t['cloud_msg'])}
{service('cyber.png', t['cyber'], t['cyber_msg'])}
{service('network.png', t['network'], t['network_msg'])}
            </div>
        </div>
        </div>
    </div>

    <div id="mu-certifications">
        <div class="container">
            <div class="cert-content">
                <h2>{t['certs']}</h2>
                <p>{t['join_msg']} <span><a href="{careers_file}">{t['join']}</a></span></p>
            </div>
        </div>
{carousel(lang, CERTS, [t['certs']] * 9)}
    </div>

    <div id="mu-reference">
        <div class="container">
            <div class="ref-content">
                <div class="ref-img"><img src="{r}assets/images/logo-grey.png" alt=""></div>
                <div class="ref-container">
                    <h2>{t['reference']}</h2>
                    <p>{t['reference_msg']}</p>
                </div>
            </div>
        </div>
{carousel(lang, CLIENTS, CLIENT_NAMES)}
    </div>
"""


def careers(lang):
    t = T[lang]; r = "../" if lang == "en" else ""
    imgs = f"""<div class="intro-img-2"><img src="{r}assets/images/rec-2.png" alt=""></div>
                    <div class="intro-img-1"><img src="{r}assets/images/rec-1.png" alt=""></div>"""
    def block(h, jobs):
        j = "\n".join(f'                            <div class="rec-job-detail"><p>{t[k]}</p></div>' for k in jobs)
        return f"""                    <div class="rec-block">
                        <h3>{h}</h3>
                        <div class="rec-job-content">
{j}
                        </div>
                    </div>"""
    return f"""    <div id="rec-intro">
        <div class="container">
            <div class="rec-content">
                <div class="intro-img-phone">
                    {imgs}
                </div>
                <div class="rec-intro-content">
                    <h2>{t['work']}</h2>
                    <p>{t['work_msg'].replace('{li}', f'<a class="linkedin-link" href="{LINKEDIN}" target="_blank" rel="noopener"><i class="fa fa-linkedin-square" aria-hidden="true"></i> ').replace('{/li}', '</a>')}</p>
                </div>
                <div class="intro-img">
                    {imgs}
                </div>
            </div>
        </div>
    </div>

    <div id="position">
        <div class="container">
            <div class="position-content">
                <div class="rec-position">
                    <h2>{t['positions']}</h2>
                    <p>{t['positions_msg']}</p>
                </div>
                <div class="rec-position-container">
                    <div class="rec-position-content">
{block(t['cloud'], ['architect','autoeng','analyst','admin','cloudsec'])}
{block(t['cyber'], ['risk','incident','operation','governance','pentest','appsec'])}
                    </div>
                    <div class="rec-position-content rec-position-content-second">
{block(t['network'], ['architect','autoeng','analyst','admin','netsec'])}
{block(t['projcs'], ['pm','am','care'])}
                    </div>
                </div>
            </div>
        </div>
    </div>
"""


REDIRECT = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8"><title>CFV Technologies</title>
<meta http-equiv="refresh" content="0; url={to}"><link rel="canonical" href="{site}{to}">
<script>location.replace("{to}");</script></head>
<body><a href="{to}">CFV Technologies</a></body></html>
"""



def main():
    for lang in ("fr", "en"):
        for page, fn in (("home", home), ("careers", careers)):
            p = OUT / PATHS[(lang, page)]
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(layout(lang, page, fn(lang)), encoding="utf-8")
    # old ASP.NET URLs keep working
    (OUT / "Home/Recruitment").mkdir(parents=True, exist_ok=True)
    (OUT / "Home/Recruitment/index.html").write_text(REDIRECT.format(to="/carrieres.html", site=SITE), encoding="utf-8")
    (OUT / "404.html").write_text(REDIRECT.format(to="/", site=SITE), encoding="utf-8")
    (OUT / "CNAME").write_text("cfvtech.com\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    urls = "".join(f"  <url><loc>{SITE}{url(l, pg)}</loc></url>\n" for l in ("fr", "en") for pg in ("home", "careers"))
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')


if __name__ == "__main__":
    main()
