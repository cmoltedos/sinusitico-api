from publish.models import User, LeadStatus, Lead, Enterprise
import datetime

def charge_users():
    init = True
    with open('publish/fake_data_csv/users.csv') as data_file:
        for line in data_file:
            if init:
                init = False
                continue
            data = line.strip().split(',')
            new_user = User()
            new_user.name = data[0] if data[0] else None
            new_user.email = data[1] if data[1] else None
            new_user.location = data[2] if data[2] else None
            new_user.user_type = data[3] if data[3] else None
            new_user.save()
    return True

def charge_leads():
    init = True
    with open('publish/fake_data_csv/leads.csv') as data_file:
        for line in data_file:
            if init:
                init = False
                continue
            data = line.strip().split(',')[1:]
            new_lead = Lead()
            new_lead.name = data[0] if data[0] else None
            new_lead.pub_date = datetime.datetime.strptime(data[1],'%d/%m/%Y') if data[1] else None
            new_lead.email = data[2] if data[2] else None
            if data[3]:
                new_lead.enterprise = Enterprise.objects.get(id=data[3])
            else:
                new_lead.enterprise = None
            new_lead.location = data[4] if data[4] else None
            new_lead.role = data[5] if data[5] else None
            new_lead.address = data[6] if data[6] else None
            new_lead.phone = data[7] if data[7] else None
            new_lead.tags = data[8] if data[8] else None
            new_lead.facebook_link = data[9] if data[9] else None
            new_lead.linkedin_link = data[10] if data[10] else None
            new_lead.instagram_link = data[11] if data[11] else None
            new_lead.oportunity = data[12] if data[12] else None
            new_lead.close_date = datetime.datetime.strptime(data[13],'%d/%m/%Y') if data[13] else None
            new_lead.save()
    return True