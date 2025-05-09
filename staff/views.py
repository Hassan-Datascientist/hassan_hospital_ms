from django.shortcuts import render
from django.http import HttpResponse





# Getting all stuff members, path: /staff/
def get_staffs(request):
    # 
    return render(request, 'staff/staff_list.html')


# path: /staff/id/
def get_staff(request, id):
    return render(request, "staff/staff_info.html") 


# path: /staff/id/
def delete_staff(request, id):
    return HttpResponse(f"Deleting a member with an {id}")



# path: /staff/id/ 
def update_staff(request, id):
    return HttpResponse(f"Updating a member with {id}")
