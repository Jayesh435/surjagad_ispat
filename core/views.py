from django.shortcuts import render


def index(request):
    news = [
        {'date': '12 Mar 2025', 'category': 'Press release', 'title': 'Surjagad Ispat commissions 1.5 GW solar park at Vijayanagar', 'read': '5 min'},
        {'date': '04 Feb 2025', 'category': 'Investor update', 'title': 'Q3 FY25 results: EBITDA crosses ₹6,200 Cr, up 18% YoY', 'read': '3 min'},
        {'date': '21 Jan 2025', 'category': 'ESG', 'title': 'First commercial green-hydrogen blast furnace trial completed', 'read': '7 min'},
        {'date': '08 Jan 2025', 'category': 'Awards', 'title': 'Surjagad Ispat named Manufacturer of the Year — Forbes Asia 200', 'read': '2 min'},
    ]
    return render(request, 'core/index.html', {
        'segments': _get_segments(),
        'news': news,
    })


def about(request):
    milestones = [
        {'year': '1924', 'text': 'Surjagad Ispat founded as a single rolling mill in western India.'},
        {'year': '1968', 'text': "Commissioned country's first integrated blast furnace complex."},
        {'year': '1992', 'text': 'Listed on the Bombay Stock Exchange.'},
        {'year': '2007', 'text': 'Acquired Italian special-steel maker Ferralto S.p.A.'},
        {'year': '2018', 'text': 'Crossed 25 MTPA — entered the global top 10 by capacity.'},
        {'year': '2024', 'text': 'Pledged $5B toward a net-zero roadmap by 2050.'},
    ]
    leaders = [
        {'name': 'Aarav Mehta', 'role': 'Chairman & Managing Director'},
        {'name': 'Sara Iyer', 'role': 'CEO, Steel Business'},
        {"name": "Rohan D'Souza", 'role': 'Chief Sustainability Officer'},
        {'name': 'Naomi Park', 'role': 'Group CFO'},
    ]
    vision_blocks = [
        {'k': 'Vision', 'v': 'To forge the materials and infrastructure of a sustainable, sovereign tomorrow.'},
        {'k': 'Mission', 'v': 'Engineer steel of uncompromising quality, at unprecedented scale, with planetary responsibility.'},
        {'k': 'Values', 'v': 'Craft. Conviction. Continuity. Three words. One hundred years.'},
    ]
    return render(request, 'core/about.html', {
        'milestones': milestones,
        'leaders': leaders,
        'vision_blocks': vision_blocks,
    })


def business(request):
    detail = [
        {'id': 'steel', 'title': 'Steel', 'img': '', 'no': '01',
         'body': 'From 41 MTPA of crude steel capacity, we deliver flat, long, and special steels to automotive OEMs, white-goods manufacturers, and infrastructure builders across six continents.'},
        {'id': 'infra', 'title': 'Infrastructure', 'img': '', 'no': '02',
         'body': "Our cement, ports, roads, and urban infrastructure businesses build the platforms upon which India's growth story is written."},
        {'id': 'energy', 'title': 'Energy', 'img': 'core/assets/esg-wind.jpg', 'no': '03',
         'body': 'A 4.2 GW captive energy portfolio combining thermal, solar, and wind — increasingly clean, increasingly self-sufficient.'},
        {'id': 'logistics', 'title': 'Logistics', 'img': 'core/assets/logistics-port.jpg', 'no': '04',
         'body': 'Dedicated rail, captive ports, and global ocean-shipping arrangements give us end-to-end command of every tonne we move.'},
    ]
    segments = _get_segments()
    return render(request, 'core/business.html', {'detail': detail, 'segments': segments})


def products(request):
    items = [
        {'img': 'core/assets/product-coils.jpg', 'name': 'Hot Rolled Coils', 'grade': 'IS 2062 / EN 10025', 'thick': '1.6 – 25 mm'},
        {'img': 'core/assets/product-sheets.jpg', 'name': 'Cold Rolled Coils', 'grade': 'IS 513 / DIN EN 10130', 'thick': '0.3 – 3.0 mm'},
        {'img': 'core/assets/product-sheets.jpg', 'name': 'Galvanized Plain', 'grade': 'IS 277', 'thick': '0.14 – 4.0 mm'},
        {'img': 'core/assets/product-structural.jpg', 'name': 'Structural Sections', 'grade': 'Fe 410 / 500 / 550', 'thick': 'Various'},
        {'img': 'core/assets/product-structural.jpg', 'name': 'TMT Bars (Neosteel)', 'grade': 'Fe 500D / 550D', 'thick': '8 – 40 mm'},
        {'img': 'core/assets/product-coils.jpg', 'name': 'Electrical Steel (CRGO)', 'grade': 'M2 – M6', 'thick': '0.23 – 0.35 mm'},
    ]
    return render(request, 'core/products.html', {'items': items})


def careers(request):
    roles = [
        {'title': 'Senior Metallurgical Engineer', 'loc': 'Vijayanagar · India', 'type': 'Full-time'},
        {'title': 'Process Lead — Cold Rolling Mill', 'loc': 'Dolvi · India', 'type': 'Full-time'},
        {'title': 'Sustainability Analyst', 'loc': 'Mumbai · India', 'type': 'Full-time'},
        {'title': 'Mining Operations Manager', 'loc': 'Pilbara · Australia', 'type': 'Full-time'},
        {'title': 'Trade Finance Lead', 'loc': 'Singapore', 'type': 'Full-time'},
        {'title': 'Graduate Engineer Trainee', 'loc': 'Multiple locations', 'type': 'Programme'},
    ]
    return render(request, 'core/careers.html', {'roles': roles})


def contact(request):
    offices = [
        {'city': 'Mumbai · HQ', 'addr': 'Surjagad Ispat Tower, BKC, Bandra East, Mumbai 400051', 'phone': '+91 22 4286 1000'},
        {'city': 'Singapore', 'addr': '1 Raffles Place, #44-02, Singapore 048616', 'phone': '+65 6735 0000'},
        {'city': 'London', 'addr': '30 St Mary Axe, London EC3A 8BF', 'phone': '+44 20 7946 0000'},
    ]
    sent = False
    if request.method == 'POST':
        sent = True
    return render(request, 'core/contact.html', {'offices': offices, 'sent': sent})


def media_page(request):
    news = [
        {'date': '12 Mar 2025', 'category': 'Press release', 'title': 'Surjagad Ispat commissions 1.5 GW solar park at Vijayanagar', 'read': '5 min'},
        {'date': '04 Feb 2025', 'category': 'Investor update', 'title': 'Q3 FY25 results: EBITDA crosses ₹6,200 Cr, up 18% YoY', 'read': '3 min'},
        {'date': '21 Jan 2025', 'category': 'ESG', 'title': 'First commercial green-hydrogen blast furnace trial completed', 'read': '7 min'},
        {'date': '08 Jan 2025', 'category': 'Awards', 'title': 'Surjagad Ispat named Manufacturer of the Year — Forbes Asia 200', 'read': '2 min'},
        {'date': '12 Mar 2025', 'category': 'Press release', 'title': 'Surjagad Ispat commissions 1.5 GW solar park at Vijayanagar', 'read': '5 min'},
        {'date': '04 Feb 2025', 'category': 'Investor update', 'title': 'Q3 FY25 results: EBITDA crosses ₹6,200 Cr, up 18% YoY', 'read': '3 min'},
        {'date': '21 Jan 2025', 'category': 'ESG', 'title': 'First commercial green-hydrogen blast furnace trial completed', 'read': '7 min'},
        {'date': '08 Jan 2025', 'category': 'Awards', 'title': 'Surjagad Ispat named Manufacturer of the Year — Forbes Asia 200', 'read': '2 min'},
    ]
    return render(request, 'core/media.html', {'news': news})


def reports(request):
    statutory_reports = [
        {'title': 'Environmental Clearance copy of Surjagad Ispat Vijayanagar Plant (25 MTPA)', 'category': 'Environmental', 'date': '2024'},
        {'title': 'Annual ESG Report FY2024-25', 'category': 'ESG Report', 'date': '2025'},
        {'title': 'Corporate Governance Report', 'category': 'Governance', 'date': '2025'},
    ]
    return render(request, 'core/reports.html', {'statutory_reports': statutory_reports})


def _get_segments():
    return [
        {'no': '01', 'icon': 'factory', 'title': 'Steel', 'desc': 'Flat, long, and special steels engineered for the most demanding applications — from automotive bodies to deep-sea pipelines.', 'capacity': '41 MTPA'},
        {'no': '02', 'icon': 'building2', 'title': 'Infrastructure', 'desc': 'Cement, ports, and roads. We build the platforms upon which economies stand.', 'capacity': '23 MTPA'},
        {'no': '03', 'icon': 'wind', 'title': 'Energy', 'desc': 'Captive thermal, solar, and wind. A 4.2 GW portfolio powering our plants and the grid.', 'capacity': '4.2 GW'},
        {'no': '04', 'icon': 'ship', 'title': 'Logistics', 'desc': "Port terminals, dedicated rail, and global shipping. Steel doesn't stand still — neither do we.", 'capacity': '60 MTPA'},
    ]
