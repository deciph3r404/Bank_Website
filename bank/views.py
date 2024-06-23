from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404, render



# Create your views here.
def index(request):
    return render(request,'index.html')
# def bank(request):
#   return render(request,'index.html')
def create_account(request): 
    if request.method == "POST":
         
        username = request.POST['username']
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return redirect('create_account')

        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        number=request.POST['number']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.email=email
        myuser.save()
        
        messages.success(request,"Your Account has been Successfully Created")

        return redirect('auth_login')
        


    return render(request,'create_account.html')
def auth_login(request):
     if request.method == 'POST':
         username=request.POST['username']
         pass1=request.POST['pass1']
         user=authenticate(request,username=username, password=pass1)
         if user is not None:
             login(request, user)
             fname=user.first_name
             return render(request,"home.html",{'fname':fname})
         else:
          messages.error(request,"Invalid Login Details")
          return redirect('auth_login')
     return render(request,'auth_login.html')

# def main(request):
#     return render(request,'main.html')
def logout(request):
    return render(request,"auth_login.html")


# my code


@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required

def account_summary_view(request):
    # Fetch account details and transactions for the logged-in user
    account_details = {
        'account_number': '71265432',
        'account_type': 'Savings',
        'ifsc_code': '3456981AEGVVE04',
        'branch': 'Main Branch',
        'current_balance': '$1,000'
    }

    transactions = [
        {'date': '01/01/2024', 'description': 'ATM Withdrawal', 'amount': '-$100', 'status': 'Completed'},
        {'date': '31/12/2023', 'description': 'Salary Credit', 'amount': '$2000', 'status': 'Completed'},
        {'date': '29/12/2023', 'description': 'Electricity Bill', 'amount': '-$150', 'status': 'Completed'},
        # Add more transactions as needed
    ]

    context = {
        'account_number': account_details['account_number'],
        'account_type': account_details['account_type'],
        'ifsc_code': account_details['ifsc_code'],
        'branch': account_details['branch'],
        'current_balance': account_details['current_balance'],
        'transactions': transactions
    }
    
    return render(request, 'account_summary.html', context)

@login_required
def transfer_money_view(request):
    if request.method == 'POST':
        from_account = request.POST.get('from_account')
        to_account = request.POST.get('to_account')
        ifsc_code = request.POST.get('ifsc_code')
        amount = request.POST.get('amount')
        remarks = request.POST.get('remarks')
        
        # Perform the transfer logic here
        # This is just a mockup, so let's assume the transfer is successful
        
        messages.success(request, 'Money transferred successfully!')
        return redirect('account_summary')
    
    return render(request, 'transfer_money.html')

@login_required
def transaction_history_view(request):
    # Fetch transactions for the logged-in user
    transactions = [
        {'date': '01/01/2024', 'description': 'ATM Withdrawal', 'amount': '-$100', 'status': 'Completed'},
        {'date': '31/12/2023', 'description': 'Salary Credit', 'amount': '$2000', 'status': 'Completed'},
        {'date': '29/12/2023', 'description': 'Electricity Bill', 'amount': '-$150', 'status': 'Completed'},
        # Add more transactions as needed
    ]

    context = {
        'transactions': transactions
    }

    return render(request, 'transaction_history.html', context)

@login_required
def pay_bills_view(request):
    if request.method == 'POST':
        bill_type = request.POST.get('bill_type')
        account_number = request.POST.get('account_number')
        amount = request.POST.get('amount')
        due_date = request.POST.get('due_date')
        
        # Perform the bill payment logic here
        # This is just a mockup, so let's assume the payment is successful
        
        messages.success(request, 'Bill paid successfully!')
        return redirect('account_summary')
    
    return render(request, 'pay_bills.html')

@login_required
def alerts_view(request):
    # Fetch alerts for the logged-in user
    alerts = [
        {'date': '01/01/2024', 'message': 'Your statement is ready for download.'},
        {'date': '31/12/2023', 'message': 'Your bill payment for $150 has been successful.'},
        {'date': '29/12/2023', 'message': 'Password was changed successfully.'},
        # Add more alerts as needed
    ]

    context = {
        'alerts': alerts
    }

    return render(request, 'alerts.html', context)

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.profile.phone = request.POST.get('phone')
        user.profile.address = request.POST.get('address')
        user.save()
        user.profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(request, 'profile.html')


@login_required
def logout_confirm_view(request):
    if request.method == 'POST':
        if 'yes' in request.POST:
            logout(request)
            return redirect('auth_login')
        elif 'no' in request.POST:
            return redirect('home')
    return render(request, 'logout_confirm.html')

