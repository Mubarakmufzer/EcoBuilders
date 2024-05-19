from urllib import request

from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login
from .send_mail import send_mail


def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')



######################################################################################
################################### ADMIN ##############################################

def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            pm_l = customer_details.objects.filter()
            msg = ''
            if len(pm_l) == 0:
                msg = 'No Customers'
            pm_2 = staff_details.objects.filter()
            msg = ''
            if len(pm_2) == 0:
                msg = 'No staff'
            pm_3 = category_master.objects.filter()
            msg = ''
            if len(pm_3) == 0:
                msg = 'No categories yet'
            pm_4 = quotation_master.objects.filter()
            msg = ''
            if len(pm_4) == 0:
                msg = 'No quotation yet'
            pm_5 = contact_us.objects.filter()
            msg = ''
            if len(pm_5) == 0:
                msg = 'No contact us yet'
            ud = customer_details.objects.all()
            ud = customer_details.objects.all()
            jm_l = staff_details.objects.all()
            t_user = len(pm_l)
            t_staff = len(pm_2)
            t_category = len(pm_3)
            t_quotation = len(pm_4)
            t_contact = len(pm_5)
            context = {'total_user': t_user, 'total_staff': t_staff, 'total_category': t_category,
                       'total_quotation': t_quotation,
                       'msg': msg, 'user_list': ud, 'type': 'User Details', 'staff_list': jm_l,'total_contact': t_contact}
            return render(request,'./myapp/admin_home.html',context)
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        pm_l = customer_details.objects.filter()
        msg = ''
        if len(pm_l) == 0:
            msg = 'No Customers'
        pm_2 = staff_details.objects.filter()
        msg = ''
        if len(pm_2) == 0:
            msg = 'No staff'
        pm_3 = category_master.objects.filter()
        msg = ''
        if len(pm_3) == 0:
            msg = 'No categories yet'
        pm_4 = quotation_master.objects.filter()
        msg = ''
        if len(pm_4) == 0:
            msg = 'No quotation yet'
        pm_5 = contact_us.objects.filter()
        msg = ''
        if len(pm_5) == 0:
            msg = 'No contact us yet'
        ud = customer_details.objects.all()
        jm_l = staff_details.objects.all()
        t_user = len(pm_l)
        t_staff = len(pm_2)
        t_category = len(pm_3)
        t_quotation = len(pm_4)
        t_contact = len(pm_5)
        context = {'total_user': t_user, 'total_staff': t_staff, 'total_category': t_category, 'total_quotation': t_quotation,
                   'msg': msg, 'user_list': ud, 'type': 'User Details', 'staff_list': jm_l,'total_contact': t_contact}
        return render(request, './myapp/admin_home.html', context)


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)

def admin_customer_details_view(request):
    u_l = customer_details.objects.all()
    msg =''
    if len(u_l) == 0:
        msg = 'No Users'
    context = {'customer_list':u_l, 'msg':msg}
    return render(request, './myapp/admin_customer_details_view.html',context)

def admin_customer_details_delete(request):
    id = request.GET.get('id')
    print("id=" + id)

    nm = customer_details.objects.get(id=int(id))
    u_l = user_login.objects.get(id=nm.user_id)
    u_l.delete()
    nm.delete()

    ul_l = user_login.objects.filter(u_type='customer')

    tm_l = []
    for u in ul_l:
        ud = customer_details.objects.get(id=u.id)
        tm_l.append(ud)
    # cd = customer_details.objects.all()
    context = {'customer_list': tm_l, 'type': 'User Details', 'msg': 'User Removed'}
    return render(request, './myapp/admin_customer_details_view.html', context)


from .models import category_master
def admin_category_details_add(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        c_d = category_master(category_name = category_name)
        c_d.save()
        context = {'msg':'category added'}
        return render(request, './myapp/admin_category_details_add.html', context)
    else:
        return render(request, './myapp/admin_category_details_add.html')

def admin_category_details_view(request):
    cl = category_master.objects.all()
    context = {'category_list':cl}
    return render(request, './myapp/admin_category_details_view.html',context)


def admin_category_details_edit(request):
    if request.method == 'POST':
        c_id = request.POST.get('c_id')
        category_name = request.POST.get('category_name')
        ctg = category_master.objects.get(id=int(c_id))
        ctg.category_name = category_name
        ctg.save()


        msg = 'Category Record Updated'
        ct_l = category_master.objects.all()
        context = {'category_list': ct_l, 'msg': msg}
        return render(request, './myapp/admin_category_details_view.html', context)
    else:
        id = request.GET.get('id')
        ct = category_master.objects.get(id=int(id))
        context = {'category_name': ct.category_name, 'c_id': ct.id}
        return render(request, './myapp/admin_category_details_edit.html',context)

def admin_category_details_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = category_master.objects.get(id=int(id))
    cg.delete()
    msg = 'Category Removed'

    ct_l = category_master.objects.all()
    context = {'category_list': ct_l, 'msg':msg}
    return render(request, './myapp/admin_category_details_view.html', context)




from .models import designation_master
def admin_designation_master_add(request):
    if request.method == 'POST':
        designation_name = request.POST.get('designation_name')
        dg = designation_master(designation_name = designation_name)
        dg.save()
        context = {'msg':'Designation added'}
        return render(request, './myapp/admin_designation_master_add.html', context)
    else:
        return render(request, './myapp/admin_designation_master_add.html')

def admin_designation_master_view(request):
    cl = designation_master.objects.all()
    context = {'desig_list':cl}
    return render(request, './myapp/admin_designation_master_view.html',context)


def admin_designation_master_edit(request):
    if request.method == 'POST':
        d_id = request.POST.get('d_id')
        designation_name = request.POST.get('designation_name')
        dgn = designation_master.objects.get(id=int(d_id))
        dgn.designation_name = designation_name
        dgn.save()


        msg = 'Designation Record Updated'
        dg_l = designation_master.objects.all()
        context = {'desig_list': dg_l, 'msg': msg}
        return render(request, './myapp/admin_designation_master_view.html', context)
    else:
        id = request.GET.get('id')
        dg = designation_master.objects.get(id=int(id))
        context = {'designation_name': dg.designation_name, 'd_id': dg.id}
        return render(request, './myapp/admin_designation_master_edit.html',context)

def admin_designation_master_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    dg = designation_master.objects.get(id=int(id))
    dg.delete()
    msg = 'Designation Removed'

    dg_l = designation_master.objects.all()
    context = {'desig_list': dg_l, 'msg':msg}
    return render(request, './myapp/admin_designation_master_view.html', context)


def admin_staff_details_view(request):
    sl = staff_details.objects.all()
    dl = designation_master.objects.all()
    context ={'staff_list':sl, 'desg_list':dl}
    return render(request, './myapp/admin_staff_details_view.html',context)


from . models import staff_details

def admin_staff_details_add(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        desg_id = request.POST.get('desg_id')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact =  request.POST.get('contact')

        uname = email
        password = '1234'
        #send_mail('Login password', '1st time password:' + password, uname)
        ul = user_login(uname=uname, passwd=password, u_type = 'staff')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        sd = staff_details(user_id=user_id, fname=fname, lname=lname, desg_id=desg_id, addr=addr, pin=pin, email=email, contact=contact )
        sd.save()
        print(user_id)
        context ={'msg':'New Staff Registered..'}
        return render(request, './myapp/admin_staff_details_add.html', context)
    else:
        ds = designation_master.objects.all()
        context = {'desg_list':ds}
        return render(request, './myapp/admin_staff_details_add.html', context)

def admin_staff_details_delete(request):
    id = request.GET.get('id')
    print('id = ' + id)
    cg = staff_details.objects.get(id=int(id))
    ud = user_login.objects.get(id=int(cg.user_id))
    ud.delete()
    cg.delete()
    msg = 'Staff Removed'
    sl = staff_details.objects.all()
    dl = designation_master.objects.all()
    # s_l = staff_details.objects.all()
    context = {'staff_list':sl, 'desg_list':dl, 'msg': msg}
    return render(request, './myapp/admin_staff_details_view.html', context)

def admin_staff_quotation_view(request):
    #user_id = request.session['user_id']
    pm_l = quotation_master.objects.filter(status='approved')
    category_list = category_master.objects.all()
    user_list = customer_details.objects.all()
    context = {'quotation_list': pm_l, 'msg': '', 'category_list': category_list,
               'user_list': user_list}
    return render(request, 'myapp/admin_staff_quotation_view.html', context)

def admin_staff_quotation_reply_view(request):
    #user_id = request.session['user_id']
    quotation_id = request.GET.get('quotation_id')
    pm_l = quotation_reply.objects.filter(quotation_id=int(quotation_id))
    user_list = staff_details.objects.all()
    context = {'qreply_list': pm_l, 'msg': '', 'quotation_id': quotation_id,
               'user_list': user_list}
    return render(request, 'myapp/admin_staff_quotation_reply_view.html', context)
#############################################################################
####################################STAFF#####################################################



def staff_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='staff')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/staff_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/staff_login.html',context)
    else:
        return render(request, 'myapp/staff_login.html')

def staff_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/staff_home.html',context)


def staff_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return staff_login(request)
    else:
        return staff_login(request)

def staff_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/staff_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/staff_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/staff_changepassword.html', context)
    else:
        return render(request, './myapp/staff_changepassword.html')

def staff_quotation_update(request):
    id = request.GET.get('id')
    status = request.GET.get('status')
    print("id="+id)

    ed = quotation_master.objects.get(id=int(id))
    ed.status = status
    ed.save()
    ud = customer_details.objects.get(user_id=int(ed.user_id))
    #print(f'.............{ud.email}')
    #send_mail('Construction Company', f'Work order {ed.q_descp}  is  {status}' , ud.email)

    pm_l = quotation_master.objects.filter(status='pending')
    category_list = category_master.objects.all()
    user_list = customer_details.objects.all()
    context ={'quotation_list': pm_l,'msg':'Updated', 'category_list':category_list,
              'user_list': user_list}
    return render(request,'myapp/staff_quotation_view.html',context)


def staff_quotation_pending_view(request):
    #user_id = request.session['user_id']
    pm_l = quotation_master.objects.filter(status='pending')
    category_list = category_master.objects.all()
    user_list = customer_details.objects.all()
    context = {'quotation_list': pm_l, 'msg': '', 'category_list': category_list,
               'user_list': user_list}
    return render(request, 'myapp/staff_quotation_view.html', context)

def staff_quotation_reject_view(request):
   # user_id = request.session['user_id']
    pm_l = quotation_master.objects.filter(status='reject')
    category_list = category_master.objects.all()
    user_list = customer_details.objects.all()
    context = {'quotation_list': pm_l, 'msg': '', 'category_list': category_list,
               'user_list': user_list}
    return render(request, 'myapp/staff_quotation_view.html', context)

def staff_quotation_view(request):
   # user_id = request.session['user_id']
    pm_l = quotation_master.objects.filter(status='approved')
    category_list = category_master.objects.all()
    user_list = customer_details.objects.all()
    context = {'quotation_list': pm_l, 'msg': '', 'category_list': category_list,
               'user_list': user_list}
    return render(request, 'myapp/staff_quotation_view.html', context)

from .models import quotation_reply
def staff_quotation_reply_add(request):
    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        plan_file = fs.save(uploaded_file.name, uploaded_file)
        remarks = request.POST.get('remarks')
        quotation_id = request.POST.get('quotation_id')
        amt = request.POST.get('amt')
        amt_details = request.POST.get('amt_details')
        esdt = request.POST.get('esdt')
        eedt = request.POST.get('eedt')
        status = 'pending'
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        user_id = request.session['user_id']

        ed = quotation_reply(user_id=int(user_id), remarks=remarks,
                            plan_file=plan_file, amt=float(amt),amt_details=amt_details,
                             quotation_id=int(quotation_id),
                           dt=dt, tm=tm,esdt=esdt,eedt=eedt)
        ed.save()

        context = {'msg':'Record added', 'quotation_id':quotation_id}
        return render(request, 'myapp/staff_quotation_reply_add.html',context)

    else:
        quotation_id = request.GET.get('quotation_id')
        context = {'msg': '', 'quotation_id': quotation_id}
        return render(request, 'myapp/staff_quotation_reply_add.html',context)


def staff_quotation_reply_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    ed = quotation_reply.objects.get(id=int(id))
    ed.delete()
    quotation_id = request.GET.get('quotation_id')
    pm_l = quotation_reply.objects.filter(quotation_id=int(quotation_id))
    user_list = staff_details.objects.all()
    context = {'qreply_list': pm_l, 'msg': 'Deleted', 'quotation_id': quotation_id,
               'user_list': user_list}
    return render(request, 'myapp/staff_quotation_reply_view.html', context)


def staff_quotation_reply_view(request):
    #user_id = request.session['user_id']
    quotation_id = request.GET.get('quotation_id')
    pm_l = quotation_reply.objects.filter(quotation_id=int(quotation_id))
    user_list = staff_details.objects.all()
    context = {'qreply_list': pm_l, 'msg': '', 'quotation_id': quotation_id,
               'user_list': user_list}
    return render(request, 'myapp/staff_quotation_reply_view.html', context)

from .models import quotation_details
def staff_quotation_details_add(request):
    if request.method == 'POST':

        remarks = request.POST.get('remarks')
        quotation_id = request.POST.get('quotation_id')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        user_id = request.session['user_id']

        ed = quotation_details(user_id=int(user_id), remarks=remarks,
                            quotation_id=int(quotation_id),
                           dt=dt, tm=tm)
        ed.save()

        context = {'msg':'Record added', 'quotation_id':quotation_id}
        return render(request, 'myapp/staff_quotation_details_add.html',context)

    else:
        quotation_id = request.GET.get('quotation_id')
        context = {'msg': '', 'quotation_id': quotation_id}
        return render(request, 'myapp/staff_quotation_details_add.html',context)


def staff_quotation_details_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    ed = quotation_reply.objects.get(id=int(id))
    ed.delete()
    quotation_id = request.GET.get('quotation_id')
    pm_l = quotation_details.objects.filter(quotation_id=int(quotation_id))
    user_list = staff_details.objects.all()
    context = {'qreply_list': pm_l, 'msg': 'Deleted', 'quotation_id': quotation_id,
               'user_list': user_list}
    return render(request, 'myapp/staff_quotation_details_view.html', context)


def staff_quotation_details_view(request):
    quotation_id = request.GET.get('quotation_id')
    pm_l = quotation_details.objects.filter(quotation_id=int(quotation_id))
    user_list = staff_details.objects.all()
    context = {'qreply_list': pm_l, 'msg': '', 'quotation_id': quotation_id,
               'user_list': user_list}
    return render(request, 'myapp/staff_quotation_details_view.html', context)

def staff_customer_details_view(request):
    u_l = customer_details.objects.all()
    msg =''
    if len(u_l) == 0:
        msg = 'No Users'
    context = {'user_list':u_l, 'msg':msg}
    return render(request, './myapp/staff_customer_details_view.html',context)

def staff_staff_details_view(request):
    sl = staff_details.objects.all()
    dl = designation_master.objects.all()
    context ={'staff_list':sl, 'desg_list':dl}
    return render(request, './myapp/staff_staff_details_view.html',context)


def staff_message_add(request):
    if request.method == 'POST':

        user1_id = request.session['user_id']
        user2_id = int(request.POST.get('user2_id'))
        msg = request.POST.get('msg')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'ok'
        suc = messages(user2_id=user2_id,user1_id=int(user1_id), msg=msg,dt=dt,tm=tm,status=status)
        suc.save()

        context = { 'msg': 'Message Send Added'}
        return render(request, './myapp/staff_home.html', context)
    else:
        user2_id = request.GET.get('user2_id')
        context = {'user2_id': user2_id, 'msg': ''}
        return render(request, './myapp/staff_message_add.html', context)

def staff_inbox_view(request):
    user_id = request.session['user_id']

    m_l = messages.objects.filter(user2_id=user_id)
    ud_l = customer_details.objects.all()
    sd_l = staff_details.objects.all()
    context = {'message_list': m_l, 'msg': '','user_list2': sd_l ,'user_list1': ud_l}
    return render(request, 'myapp/staff_inbox_view.html', context)

def staff_outbox_view(request):
    user_id = request.session['user_id']

    m_l = messages.objects.filter(user1_id=user_id)
    ud_l = customer_details.objects.all()
    sd_l = staff_details.objects.all()
    context = {'message_list': m_l, 'msg': '','user_list1': sd_l ,'user_list2': ud_l}
    return render(request, 'myapp/staff_outbox_view.html', context)

def staff_edit_profile(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        up = staff_details.objects.get(user_id=int(user_id))
        ul =user_login.objects.get(id=int(user_id))

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        up.fname = fname
        up.lname = lname
        up.addr = addr
        up.pin = pin
        up.contact = contact
        up.email = email
        up.save()
        ul.uname=email
        ul.save()


        print(user_id)
        context = {'msg': 'staff Details Updated','up':up}
        return render(request, 'myapp/staff_edit_profile.html',context)

    else:
        user_id = request.session['user_id']
        up = staff_details.objects.get(user_id = int(user_id))
        context={'up':up}
        return render(request, 'myapp/staff_edit_profile.html',context)

def staff_profile_view(request):
    user_id = request.session['user_id']
    sl = staff_details.objects.filter(user_id=user_id)
    dl = designation_master.objects.all()
    context ={'staff_list':sl, 'desg_list':dl}
    return render(request, './myapp/staff_profile_view.html',context)


###########################################################################################
####################################CUSTOMER#####################################################


from .models import customer_details
def customer_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='customer')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            # send_mail('Login','Welcome to Eco builders',uname)
            return render(request, 'myapp/customer_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/customer_login.html',context)
    else:
        return render(request, 'myapp/customer_login.html')


def customer_home(request):
    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/customer_home.html',context)


def customer_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        if user_login.objects.filter(uname=uname, u_type='customer').exists():
            context = {'msg': 'Username already exists'}
            return render(request, 'myapp/customer_details_add.html', context)
        else:
            #send_mail('Successfully Registered','Welcome to Eco builders',uname)
            ul = user_login(uname=uname, passwd=password, u_type='customer')
            ul.save()
            user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

            cd = customer_details(user_id=user_id,fname=fname, lname=lname, gender=gender, dob=dob,addr=addr, pin=pin, contact=contact, email=email )
            cd.save()

        print(user_id)
        context = {'msg': 'Customer Registered'}
        return render(request, 'myapp/customer_login.html',context)

    else:
        return render(request, 'myapp/customer_details_add.html')

def customer_details_update(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        up = customer_details.objects.get(user_id=int(user_id))

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        #profile_name = request.POST.get('profile_name')
        #aadhaar_no = request.POST.get('aadhaar_no')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        status = "new"

        up.fname = fname
        up.lname = lname
        up.gender = gender
        up.addr = addr
        up.pin = pin
        up.contact = contact
        up.dob = dob

        up.email = email
        up.save()


        print(user_id)
        context = {'msg': 'User Details Updated','up':up}
        return render(request, 'myapp/customer_details_update.html',context)

    else:
        user_id = request.session['user_id']
        up = customer_details.objects.get(user_id = int(user_id))
        context={'up':up}
        return render(request, 'myapp/customer_details_update.html',context)

def customer_profile_view(request):
    user_id = request.session['user_id']
    sl = customer_details.objects.filter(user_id=user_id)

    context ={'customer_list':sl}
    return render(request, './myapp/customer_profile_view.html',context)



def customer_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return customer_login(request)
    else:
        return customer_login(request)



def customer_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/customer_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/customer_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/customer_changepassword.html', context)
    else:
        return render(request, './myapp/customer_changepassword.html')



from .models import messages
from datetime import datetime
def customer_message_add(request):
    if request.method == 'POST':

        user1_id = request.session['user_id']
        user2_id = int(request.POST.get('user2_id'))
        msg = request.POST.get('msg')
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'ok'
        suc = messages(user2_id=user2_id,user1_id=int(user1_id), msg=msg,dt=dt,tm=tm,status=status)
        suc.save()

        context = { 'msg': 'Message Send Added'}
        return render(request, './myapp/customer_home.html', context)
    else:
        user2_id = request.GET.get('user2_id')
        context = {'user2_id': user2_id, 'msg': ''}
        return render(request, './myapp/customer_message_add.html', context)

def customer_inbox_view(request):
    user_id = request.session['user_id']

    m_l = messages.objects.filter(user2_id=user_id)
    ud_l = customer_details.objects.all()
    sd_l = staff_details.objects.all()
    context = {'message_list': m_l, 'msg': '','user_list1': sd_l ,'user_list2': ud_l}
    return render(request, 'myapp/customer_inbox_view.html', context)

def customer_outbox_view(request):
    user_id = request.session['user_id']

    m_l = messages.objects.filter(user1_id=user_id)
    ud_l = customer_details.objects.all()
    sd_l = staff_details.objects.all()
    context = {'message_list': m_l, 'msg': '','user_list2': sd_l ,'user_list1': ud_l}
    return render(request, 'myapp/customer_outbox_view.html', context)

from .models import quotation_master
from django.core.files.storage import FileSystemStorage
def customer_quotation_add(request):
    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        q_file = fs.save(uploaded_file.name, uploaded_file)
        q_descp = request.POST.get('q_descp')
        category_id = request.POST.get('category_id')
        tags = request.POST.get('tags')
        status = 'pending'
        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')

        user_id = request.session['user_id']

        ed = quotation_master(user_id=int(user_id), q_descp=q_descp,
                           category_id=int(category_id), q_file=q_file,
                           dt=dt, tm=tm,status=status)
        ed.save()
        category_list = category_master.objects.all()
        context = {'msg':'Record added', 'category_list':category_list}
        return render(request, 'myapp/customer_quotation_add.html',context)

    else:
        category_list = category_master.objects.all()
        context = {'msg': '', 'category_list': category_list}
        return render(request, 'myapp/customer_quotation_add.html',context)


def customer_quotation_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    ed = quotation_master.objects.get(id=int(id))
    ed.delete()

    user_id = request.session['user_id']
    pm_l = quotation_master.objects.filter(user_id=int(user_id))
    category_list = category_master.objects.all()
    user_list = customer_details.objects.all()
    context ={'quotation_list': pm_l,'msg':'Record deleted', 'category_list':category_list,
              'user_list': user_list}
    return render(request,'myapp/customer_quotation_view.html',context)


def customer_quotation_view(request):
    user_id = request.session['user_id']
    pm_l = quotation_master.objects.filter(user_id=int(user_id))
    category_list = category_master.objects.all()
    user_list = customer_details.objects.all()
    context = {'quotation_list': pm_l, 'msg': '', 'category_list': category_list,
               'user_list': user_list}
    return render(request, 'myapp/customer_quotation_view.html', context)

def customer_quotation_reply_view(request):
    #user_id = request.session['user_id']
    quotation_id = request.GET.get('quotation_id')
    pm_l = quotation_reply.objects.filter(quotation_id=int(quotation_id))
    user_list = staff_details.objects.all()
    context = {'qreply_list': pm_l, 'msg': '', 'quotation_id': quotation_id,
               'user_list': user_list}
    return render(request, 'myapp/customer_quotation_reply_view.html', context)

def customer_quotation_details_view(request):
    quotation_id = request.GET.get('quotation_id')
    pm_l = quotation_details.objects.filter(quotation_id=int(quotation_id))
    user_list = staff_details.objects.all()
    context = {'qreply_list': pm_l, 'msg': '', 'quotation_id': quotation_id,
               'user_list': user_list}
    return render(request, 'myapp/customer_quotation_details_view.html', context)

#########################################################################################
from .models import contact_us
def contact_us_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')

        cu = contact_us(name=name, subject=subject, msg=msg, email=email)
        cu.save()
        context = {'msg':' message sent'}
        return render(request, './myapp/contact_us.html', context)
    else:
        return render(request, './myapp/contact_us.html')

def admin_contact_view(request):

    sl = contact_us.objects.all()

    context ={'contact_list':sl}

    return render(request, './myapp/admin_contact_view.html', context)

def admin_contact_view_delete(request):

    id = request.GET.get('id')
    dg = contact_us.objects.get(id=id)
    dg.delete()
    c_u = contact_us.objects.all()
    msg = 'contact Removed'


    context = { 'msg': msg, 'contact_list': c_u}
    return render(request, './myapp/admin_contact_view.html', context)


def staff_quotation_delete(request):
    quotation_id = request.GET.get('quotation_id')
    qm = quotation_master.objects.get(id=quotation_id)
    qm.delete()

    pm_l = quotation_master.objects.filter(status='reject')
    category_list = category_master.objects.all()
    user_list = customer_details.objects.all()
    context = {'quotation_list': pm_l, 'msg': 'record deleted', 'category_list': category_list,
               'user_list': user_list}
    return render(request, 'myapp/staff_quotation_view.html', context)
