from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
from .models import ConsumerComplaint
from .forms import ConsumerForm,SignUpForm
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
import datetime
import uuid

# Create your views here.

MERCHANT_KEY = 'bKMfNxPPf_QdZppa'

class HomeView(TemplateView):
	template_name = 'home.html'

class LibraryView(TemplateView):
	template_name = 'library.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ConsumerListView(LoginRequiredMixin,ListView):
	model = ConsumerComplaint
	def get_queryset(self):
	    return ConsumerComplaint.objects.filter(user=self.request.user)

class ConsumerDetailView(LoginRequiredMixin,DetailView):
	model = ConsumerComplaint

class CreateConsumerView(LoginRequiredMixin,CreateView):

	form_class = ConsumerForm

	model = ConsumerComplaint

	def get_success_url(self):
		self.object.user = self.request.user
		self.object.save()
		return reverse("consumer:detail_c",kwargs={'pk':self.object.cc_id})

class UpdateConsumerView(LoginRequiredMixin,UpdateView):

	form_class = ConsumerForm

	model = ConsumerComplaint

	def get_success_url(self):
		self.object.update_flag = 1
		self.object.save()
		return reverse("consumer:detail_c",kwargs={'pk':self.object.cc_id})



def payment(request, pk):
	if request.method=="POST":
		c_obj = ConsumerComplaint.objects.get(pk=pk)
		c_obj.c_amt = request.POST.get('price', '')
		c_obj.save()

		temp = str(c_obj.cc_id)
		o_id = str(uuid.uuid4())
		if c_obj.p_status == 1:
			o_id = str(c_obj.new_cid)

		param_dict={

			'MID': 'DIY12386817555501617',
			'ORDER_ID': o_id,
			'TXN_AMOUNT': str(c_obj.c_amt),
			'CUST_ID': c_obj.o_email,
			'INDUSTRY_TYPE_ID': 'Retail',
			'WEBSITE': 'WEBSTAGING',
			'CHANNEL_ID': 'WEB',
			'CALLBACK_URL':'http://127.0.0.1:8000/consumer/' + temp + '/' + 'handlerequest/',
		}
		param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

		return render(request, 'divorce/paytm.html',   {'param_dict': param_dict})

	return render(request,'divorce/payment.html')



@csrf_exempt
def handlerequest(request, pk):
	form = request.POST
	response_dict = {}
	for i in form.keys():
		response_dict[i] = form[i]
		if i == 'CHECKSUMHASH':
			checksum = form[i]

	verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
	if verify:
		if response_dict['RESPCODE'] == '01':
			c_obj = ConsumerComplaint.objects.get(pk=pk)
			c_obj.p_status = 1
			c_obj.new_cid = response_dict['ORDERID']
			c_obj.txn_id = response_dict['TXNID']
			c_obj.p_date = response_dict['TXNDATE']
			c_obj.admin_reply = 'Accepted'
			c_obj.save()
		else:
			print('order was not successful because' + response_dict['RESPMSG'])
	return render(request, 'divorce/paymentstatus.html', {'response': response_dict})
