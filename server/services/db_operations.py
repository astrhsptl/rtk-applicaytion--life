from rest_framework.response import Response
from rest_framework import status

from changes.models import Change
from application.models import Application, ApplicationStatus, ApplicationState
from authsystem.models import User
from application.serializers import ApplicationSerializer


from server.jwt import JWTAuthClass

def make_chage(request):
    try:
        manager = User.objects.get(pk=request.data.get("manager"))
        state = ApplicationState.objects.get(pk=request.data.get("current_state"))
        create_date = request.data.get("create_date")
        application = Application.objects.get(pk=request.data.get("application"))

        former_status = application.current_status

        application.current_status = ApplicationStatus.objects.get(pk=request.data.get("current_status"))
        application.finaled_date = create_date
        application.state = state

        change=Change(
            manager=manager,
            application=application,
            current_status=application.current_status,
            former_status=former_status,
            current_state=state,
            create_date=create_date,
            )
        application.save()
        change.save()
        return Response({"detail": "successfuly saved"},status=status.HTTP_201_CREATED) 
    except:
        return Response({"detail": "troubles with json"},status=status.HTTP_400_BAD_REQUEST) 
    

def r(**params):
    resp = lambda x : Response(ApplicationSerializer(x, many=True).data, status=status.HTTP_202_ACCEPTED)
    try:
        return resp(filter(lambda m: m.marked, Application.objects.filter(**params)))
    except:
        return Response({'detail': 'invalid itn'}, status=status.HTTP_400_BAD_REQUEST)

def application_get(status_set, number, itn, company_id):
    resp = lambda x : Response(ApplicationSerializer(x, many=True).data, status=status.HTTP_202_ACCEPTED)

    if not status_set is None:
        if number:
            return r(number__contains=number, current_status__is_finaled=bool(int(status_set)))
            
        elif itn:
            return r(client=User.objects.get(itn=itn), current_status__is_finaled=bool(int(status_set)))

        elif company_id:
            return r(client=User.objects.get(id=company_id), current_status__is_finaled=bool(int(status_set)))
        return r(current_status__is_finaled=bool(int(status_set)))
    
    else:
        if number:
            return r(number__contains=number)
            
        elif itn:
            return r(client=User.objects.get(itn=itn))

        elif company_id:
            return r(client=User.objects.get(id=company_id))

        return resp(filter(lambda x: True, Application.objects.all()))
