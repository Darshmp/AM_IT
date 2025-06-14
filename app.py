# app.py (updated)
from flask import Flask, make_response, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Case study data
CASE_STUDIES = {
    "admin-suite": {
        "title": "Enterprise Administrative Suite",
        "subtitle": "Comprehensive system integrating document management, workflow automation, and executive dashboards",
        "category": "Administrative",
        "overview": "Developed a custom administrative suite for a large corporation to streamline their internal processes and improve operational efficiency.",
        "stats": [
            {"icon": "chart-line", "value": "75%", "label": "process efficiency gain"},
            {"icon": "clock", "value": "30h/week", "label": "time saved"},
            {"icon": "users", "value": "500+", "label": "employees using system"}
        ],
        "challenge": "The client was struggling with disparate systems for document management, workflow approvals, and executive reporting. This led to inefficiencies, data silos, and difficulty in tracking processes across departments.",
        "solution": "We developed an integrated platform that combined all administrative functions into a single, user-friendly interface with role-based access and automated workflows.",
        "features": [
            "Custom document management with version control",
            "Automated approval workflows with notifications",
            "Real-time executive dashboards with KPI tracking",
            "Integration with existing HR and ERP systems",
            "Mobile access for approvals on-the-go"
        ],
        "results": "The implementation resulted in a 75% reduction in process cycle times, eliminated paper-based workflows, and provided executives with real-time visibility into operations. The system also reduced administrative overhead by approximately 30 hours per week across the organization."
    },
    "attendance-system": {
        "title": "Biometric Attendance System",
        "subtitle": "Multi-modal system with facial recognition, fingerprint scanning, and mobile check-in capabilities",
        "category": "HR Tech",
        "overview": "Created a comprehensive attendance tracking solution for a manufacturing company with multiple locations and shift patterns.",
        "stats": [
            {"icon": "user-shield", "value": "99.7%", "label": "accuracy rate"},
            {"icon": "money-bill-wave", "value": "40%", "label": "payroll error reduction"},
            {"icon": "clock", "value": "100%", "label": "real-time tracking"}
        ],
        "challenge": "The client was facing issues with buddy punching, inaccurate time records, and manual data entry errors that led to payroll discrepancies and compliance risks.",
        "solution": "We implemented a multi-factor biometric system that could handle high-volume employee check-ins across multiple locations with minimal latency.",
        "features": [
            "Facial recognition with anti-spoofing technology",
            "Fingerprint scanning as backup authentication",
            "Mobile app for remote check-in/check-out",
            "Real-time reporting and alerts",
            "Integration with payroll systems"
        ],
        "results": "The system achieved 99.7% accuracy in attendance tracking, reduced payroll processing errors by 40%, and eliminated buddy punching entirely. It also provided management with real-time visibility into workforce attendance across all locations."
    },
    "user-access-management": {
        "title": "Role-Based Access Control System",
        "subtitle": "Enterprise-grade UAM with multi-factor authentication and privilege escalation monitoring",
        "category": "Security",
        "overview": "Implemented a comprehensive user access management solution for a financial services company to meet strict compliance requirements.",
        "stats": [
            {"icon": "shield-alt", "value": "Zero", "label": "security breaches"},
            {"icon": "tachometer-alt", "value": "60%", "label": "faster provisioning"},
            {"icon": "user-clock", "value": "100%", "label": "compliance audit pass"}
        ],
        "challenge": "The client needed to implement strict access controls across multiple systems while maintaining operational efficiency and meeting regulatory requirements for financial data protection.",
        "solution": "We designed a centralized access management system with role-based permissions, just-in-time provisioning, and comprehensive audit trails.",
        "features": [
            "Multi-factor authentication integration",
            "Automated user provisioning/deprovisioning",
            "Privilege escalation monitoring",
            "Real-time access reporting",
            "Integration with Active Directory and HR systems"
        ],
        "results": "The system achieved 100% compliance with regulatory audits, reduced access provisioning time by 60%, and eliminated unauthorized access incidents. It also provided complete visibility into user permissions across all systems."
    },
    "billing-system": {
        "title": "Automated Billing System",
        "subtitle": "AI-powered invoicing with contract lifecycle management and payment tracking",
        "category": "Administrative",
        "overview": "Developed an intelligent billing platform for a SaaS company to automate their invoicing and payment collection processes.",
        "stats": [
            {"icon": "robot", "value": "90%", "label": "auto-processing"},
            {"icon": "calendar-check", "value": "45%", "label": "on-time payments increase"},
            {"icon": "money-bill-wave", "value": "30%", "label": "revenue cycle reduction"}
        ],
        "challenge": "The client's manual billing processes led to delayed invoices, payment collection issues, and revenue recognition challenges. They needed a system that could handle complex pricing models and contract terms.",
        "solution": "We built an AI-powered billing engine that automatically generates invoices based on contract terms, usage data, and pricing rules, with integrated payment processing.",
        "features": [
            "Dynamic invoice generation based on contract terms",
            "Usage-based billing with real-time metering",
            "Automated payment collection and reconciliation",
            "Revenue recognition and reporting",
            "Self-service customer portal for billing inquiries"
        ],
        "results": "The system automated 90% of billing processes, improved on-time payments by 45%, and reduced the revenue cycle by 30%. It also provided finance teams with real-time revenue visibility and forecasting capabilities."
    },
    "leave-management": {
        "title": "Leave Management System",
        "subtitle": "Integrated platform with policy engine, manager approvals, and accrual calculations",
        "category": "HR Systems",
        "overview": "Created a comprehensive leave management solution for a multinational corporation with complex leave policies across different regions.",
        "stats": [
            {"icon": "exchange-alt", "value": "2-way", "label": "calendar sync"},
            {"icon": "clipboard-check", "value": "80%", "label": "faster approvals"},
            {"icon": "globe", "value": "15", "label": "countries supported"}
        ],
        "challenge": "The company had inconsistent leave tracking across regions, manual approval processes, and difficulty ensuring compliance with local labor laws. Employees struggled to understand their leave balances and entitlements.",
        "solution": "We developed a centralized leave management system with regional policy configurations, automated accruals, and manager approval workflows.",
        "features": [
            "Configurable leave policies by country/region",
            "Automated accrual calculations",
            "Manager approval workflows with delegation",
            "Employee self-service portal",
            "Integration with HRIS and calendar systems"
        ],
        "results": "The system standardized leave management across 15 countries, reduced approval times by 80%, and eliminated manual accrual calculations. It also provided HR with real-time visibility into workforce availability."
    },
    "client-portal": {
        "title": "Client Portal System",
        "subtitle": "White-labeled portal with document sharing, messaging, and service tracking",
        "category": "Custom Solution",
        "overview": "Built a secure client portal for a professional services firm to improve client communication and service delivery visibility.",
        "stats": [
            {"icon": "users", "value": "500+", "label": "active users"},
            {"icon": "comments", "value": "70%", "label": "fewer support tickets"},
            {"icon": "thumbs-up", "value": "92%", "label": "client satisfaction"}
        ],
        "challenge": "The firm relied on email and phone for client communications, leading to information silos, version control issues with documents, and limited visibility into service delivery status.",
        "solution": "We created a branded client portal with secure document sharing, messaging, project tracking, and billing visibility.",
        "features": [
            "White-labeled portal with client branding",
            "Secure document sharing with version control",
            "Real-time project status updates",
            "Integrated messaging and notifications",
            "Customizable dashboards and reports"
        ],
        "results": "The portal was adopted by 500+ users across client organizations, reduced support tickets by 70%, and improved client satisfaction to 92%. It also streamlined internal operations by centralizing client communications."
    }
}

@app.route('/')
def home():
    # Check if splash has been shown
    splash_shown = request.cookies.get('splash_shown')
    if not splash_shown:
        return redirect(url_for('splash'))
    
    current_year = datetime.now().year
    return render_template('index.html', current_year=current_year)

@app.route('/splash')
def splash():
    response = make_response(render_template('splash.html'))
    # Set cookie to remember splash has been shown
    response.set_cookie('splash_shown', 'true', max_age=86400)  # 1 day
    return response

@app.route('/case-study/<case_id>')
def case_study(case_id):
    study = CASE_STUDIES.get(case_id)
    if not study:
        return "Case study not found", 404
    
    current_year = datetime.now().year
    
    # Determine which template to use based on case_id
    if case_id == "admin-suite":
        return render_template('admin_suite.html', study=study, current_year=current_year)
    elif case_id == "attendance-system":
        return render_template('attendance_system.html', study=study, current_year=current_year)
    elif case_id == "user-access-management":
        return render_template('user_access_management.html', study=study, current_year=current_year)
    elif case_id == "billing-system":
        return render_template('billing_system.html', study=study, current_year=current_year)
    elif case_id == "leave-management":
        return render_template('leave_management.html', study=study, current_year=current_year)
    elif case_id == "client-portal":
        return render_template('client_portal.html', study=study, current_year=current_year)
    
    return render_template('case_study.html', study=study, current_year=current_year)

# Add these new routes to your app.py

@app.route('/consultation')
def consultation():
    current_year = datetime.now().year
    return render_template('consultation.html', current_year=current_year)

@app.route('/start-project')
def start_project():
    current_year = datetime.now().year
    return render_template('project_start.html', current_year=current_year)

@app.route('/submit-consultation', methods=['POST'])
def submit_consultation():
    # Process form data here (you'll need to implement this)
    # For now, just redirect to a thank you page or back to home
    return redirect(url_for('home'))

@app.route('/submit-project', methods=['POST'])
def submit_project():
    # Process form data here (you'll need to implement this)
    # For now, just redirect to a thank you page or back to home
    return redirect(url_for('home'))

@app.route('/live-chat')
def live_chat():
    current_year = datetime.now().year
    return render_template('live_chat.html', current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True)
