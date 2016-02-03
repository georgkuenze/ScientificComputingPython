# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 00:10:42 2015

@author: Georg
"""

class Person:
    def __init__(self, first_name, last_name, address=None, phone=None, birth_date=None, 
                 nationality=None):
        if isinstance(first_name, str) and isinstance(last_name, str):
            self.first_name = first_name
            self.last_name  = last_name
        else:
            raise TypeError('Name must be provided as string.')
        
        if isinstance(address, str) or address == None:
            self.address    = address
        else:
            raise TypeError('Address must be provided as string.')
        
        if isinstance(phone, str) or phone == None:
            self.phone      = phone
        else:
            raise TypeError('Phone number must be provided as string.')
            
        if isinstance(nationality, str) or nationality == None:
            self.nation     = nationality
        else:
            raise TypeError('Nationality must be provided as string.')
        
        from datetime import datetime      
        dateformat = '%Y-%m-%d'
        if isinstance(birth_date, str):
            self.birth_date = datetime.strptime(birth_date, dateformat)
        elif birth_date == None:
            self.birth_date = birth_date
        else:
            raise TypeError('Birth date must be provided as string.')
    
    def add_address(self, address):
        if isinstance(address, str):
            self.add_address = address
        else:
            raise TypeError('Address must be provided as string.')
        
    def add_phone(self, number):
        if isinstance(number, str):
            self.phone = number
        else:
            raise TypeError('Phone number must be provided as string.')
        
    def add_birth_date(self, date):
        from datetime import datetime
        dateformat = '%Y-%m-%d'
        if isinstance(date, str):
            self.birth_date = datetime.strptime(date, dateformat)
        else:
            raise TypeError('Date must be provided as string.')
    
    def add_nationality(self, nation):
        if isinstance(nation, str):
            self.nation = nation
        else:
            raise TypeError('Nationality must be provided as string.')
    
    #def __str__(self):
        #s      = 'Class: %s\n' % self.__class__.__name__
        #if hasattr(self, 'first_name') and self.first_name is not None:
        #    s += 'First name:       %s\n' % self.first_name
        #if hasattr(self, 'last_name') and self.last_name is not None:
        #    s += 'Last name:        %s\n' % self.last_name
        #if hasattr(self, 'nation') and self.nation is not None:
        #    s += 'Nationality:      %s\n' % self.nation
        #if hasattr(self, 'birth_date') and self.birth_date is not None:
        #    s += 'Birth date:       %s\n' % self.birth_date.date()
        #if hasattr(self, 'address') and self.address is not None:
        #    s += 'Address:          %s\n' % self.address
        #if hasattr(self, 'phone') and self.phone is not None:
        #    s += 'Phone:            %s\n' % self.phone

        #return s
    
    def __str__(self):
        s  = 'Class: %s\n' % self.__class__.__name__
        s += 'First name:       %s\n' % self.first_name
        s += 'Last name:        %s\n' % self.last_name
        s += 'Nationality:      %s\n' % self.nation
        if self.birth_date is not None:
            s += 'Birth date:       %s\n' % self.birth_date.date()
        else:
            s += 'Birth date:       %s\n' % self.birth_date
        s += 'Address:          %s\n' % self.address
        s += 'Phone no.:        %s\n' % self.phone
        
        return s
    
class Worker(Person):
    def __init__(self, first_name, last_name, address=None, phone=None, birth_date=None, 
                 nationality=None, company=None, company_address=None, job_phone=None):
        
        Person.__init__(self, first_name, last_name, address=None, phone=None, birth_date=None, 
                 nationality=None)
        
        if isinstance(company, str) or company == None:
            self.company = company
        else:
            raise TypeError('Company must be provided as string.')
        
        if isinstance(company_address, str) or company_address == None:
            self.company_address = company_address
        else:
            raise TypeError('Company address must be provided as string.')
        
        if isinstance(job_phone, str) or job_phone == None:
            self.job_phone = job_phone
        else:
            raise TypeError('Job phone number must be provided as string.')
    
    def add_company(self, company):
        if isinstance(company, str):
            self.company = company
        else:
            raise TypeError('Company must be provided as string.')
        
    def add_company_address(self, company_address):
        if isinstance(company_address, str):
            self.company_address = company_address
        else:
            raise TypeError('Company address must be provided as string.')
    
    def job_phone_number(self, job_phone):
        if isinstance(job_phone, str):
            self.job_phone = job_phone
        else:
            raise TypeError('Job phone number must be provided as string.')
    
    def __str__(self):
        s  = '\n'
        s += 'Company:          %s\n' % self.company
        s += 'Company address:  %s\n' % self.company_address
        s += 'Job phone no.:    %s\n' % self.job_phone
        
        return Person.__str__(self) + s

class Scientist(Worker):
    def __init__(self, first_name, last_name, address=None, phone=None, birth_date=None, 
                 nationality=None, company=None, company_address=None, job_phone=None,
                 discipline=None, science_type=None):
        
        Worker.__init__(self, first_name, last_name, address=None, phone=None, birth_date=None, 
                 nationality=None, company=None, company_address=None, job_phone=None)
        
        if isinstance(discipline, str) or discipline == None:
            self.discipline = []
            self.discipline.append(discipline)
        elif isinstance(discipline, (list, tuple)):
            self.discipline = discipline
        else:
            raise TypeError('Discipline must be provided as string, tuple or list.')
        
        if isinstance(science_type, str) or science_type == None:
            self.type = []
            self.type.append(science_type)
        elif isinstance(science_type, (list, tuple)):
            self.type = science_type
        else:
            raise TypeError('Scientific type must be provided as string, tuple or list.')
    
    def add_discipline(self, discipline):
        if isinstance(discipline, str):
            if None not in self.discipline:
                self.discipline.append(discipline)
            else:
                self.discipline = []
                self.discipline.append(discipline)
        elif isinstance(discipline, (list, tuple)):
            if None not in self.discipline:
                self.discipline += discipline
            else:
                self.discipline = discipline
        else:
            raise TypeError('Discipline must be provided as string, tuple or list.')
    
    def add_science_type(self, science_type):
        if isinstance(science_type, str):
            if None not in self.type:
                self.type.append(science_type)
            else:
                self.type = []
                self.type.append(science_type)
        elif isinstance(science_type, (list, tuple)):
            if None not in self.type:
                self.type += science_type
            else:
                self.type = science_type
        else:
            raise TypeError('Scientific type must be provided as string, tuple or list.')
    
    def __str__(self):
        s  = '\n'
        s += 'Discipline:       %s\n' % ', '.join([str(i) for i in self.discipline])
        s += 'Scientist type :  %s\n' % ', '.join([str(i) for i in self.type])
        
        return Worker.__str__(self) + s
        
class Researcher(Scientist):
    pass

class PostDoc(Scientist):
    pass

class Professor(Scientist):
    pass

__all__ = ['Person', 'Worker', 'Scientist', 'Researcher', 'PostDoc', 'Professor']