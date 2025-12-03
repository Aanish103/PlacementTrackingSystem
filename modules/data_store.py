#placement staff data

placement_staffs = [
    {"staff_id": "PS001", "name": "John Admin", "email": "john@uni.com", "phone": "900001", "role": "Officer"},
    {"staff_id": "PS002", "name": "Sara Lee", "email": "sara@uni.com", "phone": "900002", "role": "Coordinator"},
    {"staff_id": "PS003", "name": "Mike Ross", "email": "mike@uni.com", "phone": "900003", "role": "Manager"},
    {"staff_id": "PS004", "name": "Emma Stone", "email": "emma@uni.com", "phone": "900004", "role": "Officer"},
    {"staff_id": "PS005", "name": "David Kim", "email": "david@uni.com", "phone": "900005", "role": "Officer"},
    {"staff_id": "PS006", "name": "Laura Hill", "email": "laura@uni.com", "phone": "900006", "role": "Officer"},
    {"staff_id": "PS007", "name": "Ali Khan", "email": "ali@uni.com", "phone": "900007", "role": "Coordinator"},
    {"staff_id": "PS008", "name": "Nina Roy", "email": "nina@uni.com", "phone": "900008", "role": "Officer"},
    {"staff_id": "PS009", "name": "Sam Young", "email": "sam@uni.com", "phone": "900009", "role": "Officer"},
    {"staff_id": "PS010", "name": "Rita Paul", "email": "rita@uni.com", "phone": "900010", "role": "Manager"},
]

#schools data

schools = [
    {"school_id": "SC001", "school_name": "City Uni", "location": "London"},
    {"school_id": "SC002", "school_name": "Tech Institute", "location": "Manchester"},
    {"school_id": "SC003", "school_name": "Global College", "location": "Birmingham"},
    {"school_id": "SC004", "school_name": "Metro Uni", "location": "Leeds"},
    {"school_id": "SC005", "school_name": "Central College", "location": "Bristol"},
    {"school_id": "SC006", "school_name": "North Uni", "location": "York"},
    {"school_id": "SC007", "school_name": "West Tech", "location": "Liverpool"},
    {"school_id": "SC008", "school_name": "East Uni", "location": "Oxford"},
    {"school_id": "SC009", "school_name": "South College", "location": "Reading"},
    {"school_id": "SC010", "school_name": "Prime Institute", "location": "Nottingham"},
]

#students data

students = [
    {"student_id": "ST001", "name": "Alice Johnson", "dob": "2002-01-01", "address": "London", "qualification": "BSc CS", "grad_year": 2024, "school_id": "SC001", "staff_id": "PS001"},
    {"student_id": "ST002", "name": "Ben Carter", "dob": "2001-02-02", "address": "Manchester", "qualification": "BSc DS", "grad_year": 2023, "school_id": "SC002", "staff_id": "PS002"},
    {"student_id": "ST003", "name": "Clara Martins", "dob": "2000-03-03", "address": "Leeds", "qualification": "BSc Cyber", "grad_year": 2022, "school_id": "SC003", "staff_id": "PS003"},
    {"student_id": "ST004", "name": "Daniel Stone", "dob": "1999-04-04", "address": "Oxford", "qualification": "BEng SE", "grad_year": 2024, "school_id": "SC004", "staff_id": "PS004"},
    {"student_id": "ST005", "name": "Emily White", "dob": "2001-05-05", "address": "York", "qualification": "MSc AI", "grad_year": 2024, "school_id": "SC005", "staff_id": "PS005"},
    {"student_id": "ST006", "name": "Frank Zhang", "dob": "2000-06-06", "address": "Bristol", "qualification": "BSc Data", "grad_year": 2023, "school_id": "SC006", "staff_id": "PS006"},
    {"student_id": "ST007", "name": "Grace Kim", "dob": "1998-07-07", "address": "Liverpool", "qualification": "BSc DB", "grad_year": 2022, "school_id": "SC007", "staff_id": "PS007"},
    {"student_id": "ST008", "name": "Hassan Ali", "dob": "2001-08-08", "address": "Oxford", "qualification": "BSc Cyber", "grad_year": 2024, "school_id": "SC008", "staff_id": "PS008"},
    {"student_id": "ST009", "name": "Ivy Reynolds", "dob": "2002-09-09", "address": "Reading", "qualification": "BSc IT", "grad_year": 2024, "school_id": "SC009", "staff_id": "PS009"},
    {"student_id": "ST010", "name": "Jason Lee", "dob": "2000-10-10", "address": "Nottingham", "qualification": "BSc Accounting", "grad_year": 2023, "school_id": "SC010", "staff_id": "PS010"},
]

#applications data

applications = [
    {"application_id": "AP001", "student_id": "ST001", "employer": "Google", "role": "SE Intern", "start_date": "2025-06-01", "end_date": "2025-09-01", "documents": ["CV.pdf"], "status": "Approved"},
    {"application_id": "AP002", "student_id": "ST002", "employer": "Amazon", "role": "Data Intern", "start_date": "2025-07-10", "end_date": "2025-10-10", "documents": ["Resume.pdf"], "status": "Pending"},
    {"application_id": "AP003", "student_id": "ST003", "employer": "IBM", "role": "Cyber Intern", "start_date": "2025-05-15", "end_date": "2025-08-20", "documents": ["CV.pdf"], "status": "Rejected"},
    {"application_id": "AP004", "student_id": "ST004", "employer": "Microsoft", "role": "Cloud Intern", "start_date": "2025-07-01", "end_date": "2025-11-01", "documents": ["CV.pdf"], "status": "Pending"},
    {"application_id": "AP005", "student_id": "ST005", "employer": "Meta", "role": "AI Intern", "start_date": "2025-06-15", "end_date": "2025-09-15", "documents": ["Portfolio.pdf"], "status": "Approved"},
    {"application_id": "AP006", "student_id": "ST006", "employer": "Tesla", "role": "Data Intern", "start_date": "2025-04-10", "end_date": "2025-08-10", "documents": ["CV.pdf"], "status": "Withdrawn"},
    {"application_id": "AP007", "student_id": "ST007", "employer": "Oracle", "role": "DB Intern", "start_date": "2025-06-01", "end_date": "2025-09-30", "documents": ["Transcript.pdf"], "status": "Pending"},
    {"application_id": "AP008", "student_id": "ST008", "employer": "Deloitte", "role": "Security Intern", "start_date": "2025-07-05", "end_date": "2025-11-05", "documents": ["CV.pdf"], "status": "Approved"},
    {"application_id": "AP009", "student_id": "ST009", "employer": "KPMG", "role": "Consultant Intern", "start_date": "2025-05-01", "end_date": "2025-09-01", "documents": ["Resume.pdf"], "status": "Pending"},
    {"application_id": "AP010", "student_id": "ST010", "employer": "PwC", "role": "Audit Intern", "start_date": "2025-06-10", "end_date": "2025-09-10", "documents": [], "status": "Approved"},
]


#assessments data

assessments = [
    {"assessment_id": "AS001", "application_id": "AP001", "assessor_name": "Dr Smith", "score": 85, "comments": "Excellent"},
    {"assessment_id": "AS002", "application_id": "AP002", "assessor_name": "Dr Jones", "score": 72, "comments": "Good"},
    {"assessment_id": "AS003", "application_id": "AP003", "assessor_name": "Dr Lee", "score": 60, "comments": "Average"},
    {"assessment_id": "AS004", "application_id": "AP004", "assessor_name": "Dr Kim", "score": 75, "comments": "Good"},
    {"assessment_id": "AS005", "application_id": "AP005", "assessor_name": "Dr Patel", "score": 90, "comments": "Excellent"},
    {"assessment_id": "AS006", "application_id": "AP006", "assessor_name": "Dr Admin", "score": 0, "comments": "Withdrawn"},
    {"assessment_id": "AS007", "application_id": "AP007", "assessor_name": "Dr Roy", "score": 70, "comments": "Good"},
    {"assessment_id": "AS008", "application_id": "AP008", "assessor_name": "Dr Martin", "score": 88, "comments": "Excellent"},
    {"assessment_id": "AS009", "application_id": "AP009", "assessor_name": "Dr Shah", "score": 65, "comments": "Average"},
    {"assessment_id": "AS010", "application_id": "AP010", "assessor_name": "Dr Singh", "score": 80, "comments": "Very Good"},
]

#visits data

visits = [
    {"visit_id": "V001", "application_id": "AP001", "visitor_name": "Mike", "visit_date": "2025-06-15", "outcome": "Successful", "notes": "Good"},
    {"visit_id": "V002", "application_id": "AP002", "visitor_name": "Sara", "visit_date": "2025-06-18", "outcome": "Concerns", "notes": "Minor delays"},
    {"visit_id": "V003", "application_id": "AP003", "visitor_name": "John", "visit_date": "2025-06-20", "outcome": "Failed", "notes": "Unsatisfied"},
    {"visit_id": "V004", "application_id": "AP004", "visitor_name": "Emma", "visit_date": "2025-06-22", "outcome": "Successful", "notes": "Good"},
    {"visit_id": "V005", "application_id": "AP005", "visitor_name": "David", "visit_date": "2025-06-25", "outcome": "Successful", "notes": "Excellent"},
    {"visit_id": "V006", "application_id": "AP006", "visitor_name": "Admin", "visit_date": "2025-06-27", "outcome": "Postponed", "notes": "Withdrawn"},
    {"visit_id": "V007", "application_id": "AP007", "visitor_name": "Ali", "visit_date": "2025-06-29", "outcome": "Concerns", "notes": "Minor issues"},
    {"visit_id": "V008", "application_id": "AP008", "visitor_name": "Nina", "visit_date": "2025-07-01", "outcome": "Successful", "notes": "Good"},
    {"visit_id": "V009", "application_id": "AP009", "visitor_name": "Sam", "visit_date": "2025-07-03", "outcome": "Concern", "notes": "Medium"},
    {"visit_id": "V010", "application_id": "AP010", "visitor_name": "Rita", "visit_date": "2025-07-05", "outcome": "Successful", "notes": "Excellent"},
]

#decisions data

decisions = [
    {"application_id": "AP001", "decision_type": "Approved", "decision_by": "PS001", "decision_comment": "Excellent", "decision_date": "2025-03-01"},
    {"application_id": "AP002", "decision_type": "Pending", "decision_by": "PS002", "decision_comment": "Under review", "decision_date": "2025-03-02"},
    {"application_id": "AP003", "decision_type": "Rejected", "decision_by": "PS003", "decision_comment": "Low GPA", "decision_date": "2025-03-03"},
    {"application_id": "AP004", "decision_type": "Pending", "decision_by": "PS004", "decision_comment": "Under review", "decision_date": "2025-03-04"},
    {"application_id": "AP005", "decision_type": "Approved", "decision_by": "PS005", "decision_comment": "Strong skills", "decision_date": "2025-03-05"},
    {"application_id": "AP006", "decision_type": "Withdrawn", "decision_by": "PS006", "decision_comment": "Student request", "decision_date": "2025-03-06"},
    {"application_id": "AP007", "decision_type": "Pending", "decision_by": "PS007", "decision_comment": "Reviewing", "decision_date": "2025-03-07"},
    {"application_id": "AP008", "decision_type": "Approved", "decision_by": "PS008", "decision_comment": "Strong interview", "decision_date": "2025-03-08"},
    {"application_id": "AP009", "decision_type": "Pending", "decision_by": "PS009", "decision_comment": "Scheduled", "decision_date": "2025-03-09"},
    {"application_id": "AP010", "decision_type": "Approved", "decision_by": "PS010", "decision_comment": "Excellent", "decision_date": "2025-03-10"},
]