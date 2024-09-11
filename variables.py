allWorker = {}
employee_id_counter = 1

positions = [
            "CEO", "CFO", "COO", "CTO", "Vice President", "Director",
            "Manager", "Supervisor", "Team Lead", "Business Analyst",
            "Marketing Manager", "Sales Manager", "Product Manager",
            "Operations Manager", "Human Resources Manager", "Financial Analyst",
            "Accountant", "Customer Service Representative", "Administrative Assistant",
            "Project Manager", "Legal Counsel", "IT Specialist", "Consultant",
            "Data Analyst", "Supply Chain Manager", "Chief Compliance Officer",
            "Chief Risk Officer", "Chief Information Officer", "Chief Marketing Officer",
            "Chief Procurement Officer", "Chief People Officer", "Chief Legal Officer",
            "Chief Revenue Officer", "Sales Representative", "Content Strategist",
            "UX Designer", "Digital Marketing Specialist", "Public Relations Manager",
            "Quality Assurance Manager", "Training and Development Manager",
            "Corporate Trainer", "Recruiter", "Event Coordinator", "Office Manager",
            "Facilities Manager", "Benefits Coordinator", "Payroll Specialist",
            "Software Engineer", "DevOps Engineer", "Security Analyst", "Network Administrator"
        ]

city = [
            "Baku", "Ganja", "Sumqayit", "Mingachevir", "Shirvan",
            "Lankaran", "Nakhchivan", "Shaki", "Yevlakh", "Shamakhi",
            "Goychay", "Zaqatala", "Khachmaz", "Quba", "Barda",
            "Aghdam", "Tartar", "Jalilabad", "Salyan", "Bilasuvar",
            "Masalli", "Sabirabad", "Astara", "Dashkasan", "Gadabay",
            "Gabala", "Qusar", "Ismayilli", "Kurdamir", "Ujar",
            "Fizuli", "Lachin", "Shusha", "Agjabadi", "Imishli",
            "Saatli", "Zangilan", "Jabrayil", "Kalbajar",
            "Aghstafa", "Aghsu", "Beylagan", "Balakan", "Goranboy",
            "Goygol", "Hajigabul", "Khojavend", "Khojaly", "Lerik",
            "Neftchala", "Oghuz", "Ordubad", "Shabran", "Siyazan",
            "Tovuz", "Yardimli", "Zardab", "Samukh", "Sadarak",
            "Sharur", "Kangarli", "Dashkasan", "Gobustan", "Absheron" ]

cityEdit = [
            "Baku", "Ganja", "Sumqayit", "Mingachevir", "Shirvan",
            "Lankaran", "Nakhchivan", "Shaki", "Yevlakh", "Shamakhi",
            "Goychay", "Zaqatala", "Khachmaz", "Quba", "Barda",
            "Aghdam", "Tartar", "Jalilabad", "Salyan", "Bilasuvar",
            "Masalli", "Sabirabad", "Astara", "Dashkasan", "Gadabay",
            "Gabala", "Qusar", "Ismayilli", "Kurdamir", "Ujar",
            "Fizuli", "Lachin", "Shusha", "Agjabadi", "Imishli",
            "Saatli", "Zangilan", "Jabrayil", "Kalbajar",
            "Aghstafa", "Aghsu", "Beylagan", "Balakan", "Goranboy",
            "Goygol", "Hajigabul", "Khojavend", "Khojaly", "Lerik",
            "Neftchala", "Oghuz", "Ordubad", "Shabran", "Siyazan",
            "Tovuz", "Yardimli", "Zardab", "Samukh", "Sadarak",
            "Sharur", "Kangarli", "Dashkasan", "Gobustan", "Absheron" ]

positions_filter = [
            "CEO", "CFO", "COO", "CTO", "Vice President", "Director",
            "Manager", "Supervisor", "Team Lead", "Business Analyst",
            "Marketing Manager", "Sales Manager", "Product Manager",
            "Operations Manager", "Human Resources Manager", "Financial Analyst",
            "Accountant", "Customer Service Representative", "Administrative Assistant",
            "Project Manager", "Legal Counsel", "IT Specialist", "Consultant",
            "Data Analyst", "Supply Chain Manager", "Chief Compliance Officer",
            "Chief Risk Officer", "Chief Information Officer", "Chief Marketing Officer",
            "Chief Procurement Officer", "Chief People Officer", "Chief Legal Officer",
            "Chief Revenue Officer", "Sales Representative", "Content Strategist",
            "UX Designer", "Digital Marketing Specialist", "Public Relations Manager",
            "Quality Assurance Manager", "Training and Development Manager",
            "Corporate Trainer", "Recruiter", "Event Coordinator", "Office Manager",
            "Facilities Manager", "Benefits Coordinator", "Payroll Specialist",
            "Software Engineer", "DevOps Engineer", "Security Analyst", "Network Administrator"
        ]