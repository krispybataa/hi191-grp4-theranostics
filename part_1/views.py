from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from . forms import *
from part_2.forms import *
from . models import *
from part_2.models import *
from part_3.models import *
from part_3.forms import *
from part_4.forms import *
from part_4.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test as userPassesTest
from django.db.models import Q

def isSuperuser(user):
    return user.is_superuser

def homePage(request):
    return render(request, 'part_1/home-page.html')

@userPassesTest(isSuperuser)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('patientList')
    else:
        form = UserCreationForm()
    return render(request, 'part_1/register-user.html', {'form' : form})

@login_required
def patientList(request):
    # Start with base queryset that only includes patients with screening data
    patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__isnull=False).distinct()
    
    # Get filter parameters
    low_risk = request.GET.get('flexCheckLowRisk')
    intermediate_risk = request.GET.get('flexCheckIntermediateRisk')
    high_risk = request.GET.get('flexCheckHighRisk')
    bone_metastasis = request.GET.get('flexCheckMetastasis')
    side_effects = request.GET.get('flexCheckSideEffect')
    #Screening fields
    prostateLS = request.GET.get('flexCheckProstateL')
    nodeLS = request.GET.get('flexCheckLNL')
    boneLS = request.GET.get('flexCheckBoneL')
    brainLS = request.GET.get('flexCheckBrainL')
    lungLS = request.GET.get('flexCheckLungL')
    liverLS = request.GET.get('flexCheckLiverL')
    #Post-therapy fields
    prostateLPT = request.GET.get('flexCheckProstateLPT')
    nodeLPT = request.GET.get('flexCheckLNLPT')
    boneLPT = request.GET.get('flexCheckBoneLPT')
    lungLPT = request.GET.get('flexCheckLungLPT')
    liverLPT = request.GET.get('flexCheckLiverLPT')
    #Follow-up fields
    prostateLFU = request.GET.get('flexCheckProstateLFU')
    nodeLFU = request.GET.get('flexCheckLNLFU')
    boneLFU = request.GET.get('flexCheckBoneLFU')
    brainLFU = request.GET.get('flexCheckBrainLFU')
    lungLFU = request.GET.get('flexCheckLungLFU')
    liverLFU = request.GET.get('flexCheckLiverLFU')

    # Build risk assessment filter
    risk_filters = Q()
    if low_risk == 'on':
        risk_filters |= Q(screening_patient__assessment__exact='Low Risk')
    if intermediate_risk == 'on':
        risk_filters |= Q(screening_patient__assessment__exact='Intermediate Risk')
    if high_risk == 'on':
        risk_filters |= Q(screening_patient__assessment__exact='High Risk')
    if risk_filters:
        patients = patients.filter(risk_filters)

    # Bone Metastasis
    if bone_metastasis == 'on':
        patients = patients.filter(screening_patient__bone_metastasis_status='Metastasis')

    # Side Effect
    if side_effects == 'on':
        patients = patients.filter(t_patient__side_effects__isnull=False)

    # Screening Filters
    screening_filters = Q()

    if prostateLS == 'on':
        screening_filters |= Q(screening_patient__gapsma_prostate_lesion_status='Present') | Q(screening_patient__fdgpetct_prostate_lesion_status='Present')

    if nodeLS == 'on':
        screening_filters |= Q(screening_patient__gapsma_lymph_node_lesion_status='Present') | Q(screening_patient__fdgpetct_lymph_node_lesion_status='Present')

    if boneLS == 'on':
        screening_filters |= Q(screening_patient__gapsma_bone_lesion_status='Present') | Q(screening_patient__fdgpetct_bone_lesion_status='Present')

    if brainLS == 'on':
        screening_filters |= Q(screening_patient__gapsma_brain_lesion_status='Present') | Q(screening_patient__fdgpetct_brain_lesion_status='Present')

    if lungLS == 'on':
        screening_filters |= Q(screening_patient__gapsma_lung_lesion_status='Present') | Q(screening_patient__fdgpetct_lung_lesion_status='Present')

    if liverLS == 'on':
        screening_filters |= Q(screening_patient__gapsma_liver_lesion_status='Present') | Q(screening_patient__fdgpetct_liver_lesion_status='Present')

    if screening_filters:
        patients = patients.filter(screening_filters)

    # Post-therapy filters
    if prostateLPT == 'on':
        patients = patients.filter(Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Prostate'))
    if nodeLPT == 'on':
        patients = patients.filter(Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Lymph Nodes'))
    if boneLPT == 'on':
        patients = patients.filter(Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Bones'))
    if lungLPT == 'on':
        patients = patients.filter(Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Lungs'))
    if liverLPT == 'on':
        patients = patients.filter(Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Liver'))

    # Follow-up filters
    fu_lesion_filters = Q()
    if prostateLFU == 'on':
        fu_lesion_filters |= (Q(fu_patient__gapsma_prostate_lesion_status='Present') | 
                             Q(fu_patient__fdgpetct_prostate_lesion_status='Present'))
    if nodeLFU == 'on':
        fu_lesion_filters |= (Q(fu_patient__gapsma_lymph_node_lesion_status='Present') | 
                             Q(fu_patient__fdgpetct_lymph_node_lesion_status='Present'))
    if boneLFU == 'on':
        fu_lesion_filters |= (Q(fu_patient__gapsma_bone_lesion_status='Present') | 
                             Q(fu_patient__fdgpetct_bone_lesion_status='Present'))
    if brainLFU == 'on':
        fu_lesion_filters |= (Q(fu_patient__gapsma_brain_lesion_status='Present') | 
                             Q(fu_patient__fdgpetct_brain_lesion_status='Present'))
    if lungLFU == 'on':
        fu_lesion_filters |= (Q(fu_patient__gapsma_lung_lesion_status='Present') | 
                             Q(fu_patient__fdgpetct_lung_lesion_status='Present'))
    if liverLFU == 'on':
        fu_lesion_filters |= (Q(fu_patient__gapsma_liver_lesion_status='Present') | 
                             Q(fu_patient__fdgpetct_liver_lesion_status='Present'))
    if fu_lesion_filters:
        patients = patients.filter(fu_lesion_filters)

    return render(request, 'part_1/patient-list.html', {'patients': patients.distinct()})

@login_required
def patientSearch(request):
    patients = Patient.objects.all()
    query = Q()

    # Handle text search
    search_query = request.GET.get('search_query', '').strip()
    if search_query:
        query &= Q(name__icontains=search_query)

    # Get all filter parameters
    low_risk = request.GET.get('flexCheckLowRisk')
    intermediate_risk = request.GET.get('flexCheckIntermediateRisk')
    high_risk = request.GET.get('flexCheckHighRisk')
    bone_metastasis = request.GET.get('flexCheckMetastasis')
    side_effects = request.GET.get('flexCheckSideEffect')
    
    # Screening Imaging
    prostateLS = request.GET.get('flexCheckProstateLS')
    nodeLS = request.GET.get('flexCheckLNLS')
    boneLS = request.GET.get('flexCheckBoneLS')
    brainLS = request.GET.get('flexCheckBrainLS')
    lungLS = request.GET.get('flexCheckLungLS')
    liverLS = request.GET.get('flexCheckLiverLS')
    
    # Post-Therapy Imaging
    prostateLPT = request.GET.get('flexCheckProstateLPT')
    nodeLPT = request.GET.get('flexCheckLNLPT')
    boneLPT = request.GET.get('flexCheckBoneLPT')
    brainLPT = request.GET.get('flexCheckBrainLPT')
    lungLPT = request.GET.get('flexCheckLungLPT')
    liverLPT = request.GET.get('flexCheckLiverLPT')
    
    # Follow-up Imaging
    prostateLFU = request.GET.get('flexCheckProstateLFU')
    nodeLFU = request.GET.get('flexCheckLNLFU')
    boneLFU = request.GET.get('flexCheckBoneLFU')
    brainLFU = request.GET.get('flexCheckBrainLFU')
    lungLFU = request.GET.get('flexCheckLungLFU')
    liverLFU = request.GET.get('flexCheckLiverLFU')

    # Risk Assessment Filter
    risk_query = Q()
    if low_risk == 'on':
        risk_query |= Q(screening_patient__assessment='Low Risk')
    if intermediate_risk == 'on':
        risk_query |= Q(screening_patient__assessment='Intermediate Risk')
    if high_risk == 'on':
        risk_query |= Q(screening_patient__assessment='High Risk')
    if risk_query:
        query &= risk_query

    # Bone Metastasis Filter
    if bone_metastasis == 'on':
        query &= Q(screening_patient__bone_metastasis_status='Metastasis')

    # Side Effects Filter
    if side_effects == 'on':
        query &= Q(t_patient__side_effects__isnull=False)

    # Screening Imaging Filters
    screening_query = Q()
    if prostateLS == 'on':
        screening_query |= Q(screening_patient__gapsma_prostate_lesion_status='Present')
    if nodeLS == 'on':
        screening_query |= Q(screening_patient__gapsma_lymph_node_lesion_status='Present')
    if boneLS == 'on':
        screening_query |= Q(screening_patient__gapsma_bone_lesion_status='Present')
    if brainLS == 'on':
        screening_query |= Q(screening_patient__gapsma_brain_lesion_status='Present')
    if lungLS == 'on':
        screening_query |= Q(screening_patient__gapsma_lung_lesion_status='Present')
    if liverLS == 'on':
        screening_query |= Q(screening_patient__gapsma_liver_lesion_status='Present')
    if screening_query:
        query &= screening_query

    # Post-Therapy Imaging Filters
    pt_query = Q()
    if prostateLPT == 'on':
        pt_query |= Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Prostate')
    if nodeLPT == 'on':
        pt_query |= Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Lymph Nodes')
    if boneLPT == 'on':
        pt_query |= Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Bones')
    if lungLPT == 'on':
        pt_query |= Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Lungs')
    if liverLPT == 'on':
        pt_query |= Q(pt_patient__isnull=False) & Q(pt_patient__lesions__icontains='Liver')
    if pt_query:
        query &= pt_query

    # Follow-up Imaging Filters
    fu_query = Q()
    if prostateLFU == 'on':
        fu_query |= Q(fu_patient__gapsma_prostate_lesion_status='Present') | Q(fu_patient__fdgpetct_prostate_lesion_status='Present')
    if nodeLFU == 'on':
        fu_query |= Q(fu_patient__gapsma_lymph_node_lesion_status='Present') | Q(fu_patient__fdgpetct_lymph_node_lesion_status='Present')
    if boneLFU == 'on':
        fu_query |= Q(fu_patient__gapsma_bone_lesion_status='Present') | Q(fu_patient__fdgpetct_bone_lesion_status='Present')
    if brainLFU == 'on':
        fu_query |= Q(fu_patient__gapsma_brain_lesion_status='Present') | Q(fu_patient__fdgpetct_brain_lesion_status='Present')
    if lungLFU == 'on':
        fu_query |= Q(fu_patient__gapsma_lung_lesion_status='Present') | Q(fu_patient__fdgpetct_lung_lesion_status='Present')
    if liverLFU == 'on':
        fu_query |= Q(fu_patient__gapsma_liver_lesion_status='Present') | Q(fu_patient__fdgpetct_liver_lesion_status='Present')
    if fu_query:
        query &= fu_query

    # Apply all filters if any are set
    if query:
        patients = patients.filter(query).distinct()

    context = {
        'patients': patients,
        'patient_count': patients.count(),
        'search_query': search_query,  # Pass back search query
        # Pass filter states back to template
        'low_risk': low_risk == 'on',
        'intermediate_risk': intermediate_risk == 'on',
        'high_risk': high_risk == 'on',
        'bone_metastasis': bone_metastasis == 'on',
        'side_effects': side_effects == 'on',
        'prostateLS': prostateLS == 'on',
        'nodeLS': nodeLS == 'on',
        'boneLS': boneLS == 'on',
        'brainLS': brainLS == 'on',
        'lungLS': lungLS == 'on',
        'liverLS': liverLS == 'on',
        'prostateLPT': prostateLPT == 'on',
        'nodeLPT': nodeLPT == 'on',
        'boneLPT': boneLPT == 'on',
        'brainLPT': brainLPT == 'on',
        'lungLPT': lungLPT == 'on',
        'liverLPT': liverLPT == 'on',
        'prostateLFU': prostateLFU == 'on',
        'nodeLFU': nodeLFU == 'on',
        'boneLFU': boneLFU == 'on',
        'brainLFU': brainLFU == 'on',
        'lungLFU': lungLFU == 'on',
        'liverLFU': liverLFU == 'on',
    }
    
    return render(request, "part_1/patient-list.html", context)

@login_required
def patientDetails(request, slug):
    patient = Patient.objects.get(slug=slug)
    physical_exam = PhysicalExam.objects.filter(patient=patient).first()
    screening = Screening.objects.filter(patient=patient).first()
    therapy = Therapy.objects.filter(patient=patient)
    post_therapy = PostTherapy.objects.filter(patient=patient)
    follow_up = FollowUp.objects.filter(patient=patient)

    context = {'patient' : patient, 'physical_exam' : physical_exam, 'screening' : screening, 'therapy' : therapy, 'post_therapy': post_therapy, 'follow_up' : follow_up}
    return render(request, 'part_1/patient-details.html', context)

@login_required
def addPatient(request):
    if request.method == "POST":
        form = AddPatient(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save()
            messages.success(request, f'Patient {patient.name} has been added successfully.')
            return redirect('patientList')
        else:
            messages.error(request, 'There was an error adding the patient. Please check the form.')
    else:
        form = AddPatient()
    
    context = {'form': form}
    return render(request, "part_1/add-patient.html", context)

@login_required
def editPatient(request, slug):
    patient = Patient.objects.get(slug=slug)

    if request.method == "POST":
        form = EditPatient(request.POST, instance=patient)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse_lazy('patientList'))
    else:
        form = EditPatient(instance=patient)

        context = {'form' : form}
        return render(request, "part_1/edit-patient.html", context)

@login_required
def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect('patientList')

@login_required
def addScreening(request, slug):
    patient = Patient.objects.get(slug=slug)
    if request.method == "POST":
        form = AddScreening(request.POST, request.FILES)
        if form.is_valid():
            build = form.save(commit=False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))
        else:
            context = {'form': form, 'patient': patient}
            return render(request, "part_1/add-screening.html", context)
    else:
        form = AddScreening()
        context = {'form': form, 'patient': patient}
        return render(request, "part_1/add-screening.html", context)

@login_required
def editScreening(request, slug, id):
    screening = Screening.objects.get(id=id)
    if request.method == "POST":
        form = EditScreening(request.POST, request.FILES, instance=screening)
        if form.is_valid():
            form.save()
            return redirect(reverse('patientDetails', kwargs={'slug':slug}))
        else:
            context = {'form': form}
            return render(request, "part_1/edit-screening.html", context)
    else:
        form = EditScreening(instance=screening)
        context = {'form': form}
        return render(request, "part_1/edit-screening.html", context)

@login_required
def deleteScreening(request, slug, id):
    screening = Screening.objects.get(id=id)
    screening.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

@login_required
def addPhysicalExam(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddPhysicalExam
    if request.method == "POST":
        form = AddPhysicalExam(request.POST)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))

    context={'form':form, 'patient': patient}
    return render(request,"part_1/add-physical-exam.html",context)

@login_required
def editPhysicalExam(request, slug, id):
    patient = Patient.objects.get(slug=slug)
    physical_exam = PhysicalExam.objects.get(id=id)
    if request.method == "POST":
        form = EditPhysicalExam(request.POST, instance=physical_exam)
        if form.is_valid():
            physical_exam = form.save(commit=False)
            physical_exam.patient = patient
            physical_exam.save()
        return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))
    else:
        form = EditPhysicalExam(instance=physical_exam)
        context = {'form' : form}
        return render(request, "part_1/edit-physical-exam.html", context)

@login_required 
def deletePhysicalExam(request, slug, id):
    physical_exam = PhysicalExam.objects.get(id=id)
    physical_exam.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

@login_required
def therapyList(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = Therapy.objects.filter(patient=patient).order_by('-pk')

    context = {'list': list, 'patient': patient}
    return render(request, 'part_2/therapy-list.html', context)

@login_required
def addTherapy(request, slug):
    patients = Patient.objects.all()
    patient = Patient.objects.get(slug=slug)
    form = AddTherapy()
    if request.method == "POST":
        form = AddTherapy(request.POST)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))
# def
    context={'form':form, 'patient': patient}
    return render(request,"part_2/add-therapy.html",context)

@login_required
def editTherapy(request, slug, id):
    therapy = Therapy.objects.get(id=id)
    if request.method == "POST":
        form = EditTherapy(request.POST, instance=therapy)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))
    else:
        form = EditTherapy(instance=therapy)
        context = {'form' : form}
        return render(request, "part_2/edit-therapy.html", context)

@login_required
def deleteTherapy(request, slug, id):
    therapy = Therapy.objects.get(id=id)
    therapy.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

@login_required
def postTherapyList(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = PostTherapy.objects.filter(patient=patient).order_by('-pk')

    context = {'list': list, 'patient': patient}
    return render(request, 'part_3/post-therapy-list.html', context)

@login_required
def addPostTherapy(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddPostTherapy()
    if request.method == "POST":
        form = AddPostTherapy(request.POST, request.FILES)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))
        
    context={'form':form, 'patient': patient}
    return render(request,"part_3/add-post-therapy.html",context)

@login_required
def editPostTherapy(request, slug, id):
    post_therapy = PostTherapy.objects.get(id=id)
    if request.method == "POST":
        form = EditPostTherapy(request.POST, instance=post_therapy)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))
    else:
        form = EditPostTherapy(instance=post_therapy)
        context = {'form' : form}
        return render(request, "part_3/edit-post-therapy.html", context)

@login_required
def deletePostTherapy(request, slug, id):
    post_therapy = PostTherapy.objects.get(id=id)
    post_therapy.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

@login_required
def followUpList(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = FollowUp.objects.filter(patient=patient).order_by('-pk')

    context = {'list': list, 'patient': patient}
    return render(request, 'part_4/follow-up-list.html', context)

@login_required
def addFollowUp(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddFollowUp()
    if request.method == "POST":
        form = AddFollowUp(request.POST, request.FILES)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))
# def
    context={'form':form, 'patient': patient}
    return render(request,"part_4/add-follow-up.html",context)

@login_required
def editFollowUp(request, slug, id):
    follow_up = FollowUp.objects.get(id=id)
    if request.method == "POST":
        form = EditFollowUp(request.POST, request.FILES, instance=follow_up)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))
        else:
            context = {'form': form}
            return render(request, "part_4/edit-follow-up.html", context)
    else:
        form = EditFollowUp(instance=follow_up)
        context = {'form': form}
        return render(request, "part_4/edit-follow-up.html", context)

@login_required
def deleteFollowUp(request, slug, id):
    follow_up = FollowUp.objects.get(id=id)
    follow_up.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

def viewPhysicalExam(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = PhysicalExam.objects.filter(patient=patient).first()

    context = {'list': list, 'patient': patient}
    return render(request, 'part_1/view-physical-exam.html', context)


def viewScreening(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = Screening.objects.filter(patient=patient).first()

    context = {'list': list, 'patient': patient}
    return render(request, 'part_1/view-screening.html', context)