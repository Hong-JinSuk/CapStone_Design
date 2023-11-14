from django.shortcuts import render,redirect,get_list_or_404
from django.http import Http404
from .models import Board
from .forms import BoardForm
from accounts.models import User
from django.core.paginator import Paginator,InvalidPage
from datetime import datetime

def ceo_board_write(request):
    # 사용자 ID를 가져옵니다.
    user_id = request.session.get('user')
    if user_id is None:
        return redirect('/ceoaccounts/ceo_login')

    # 사용자 객체를 가져옵니다.
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return redirect('/ceoaccounts/ceo_login')

    # 게시물을 작성합니다.
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = Board(
                title=form.cleaned_data['title'],
                contents=form.cleaned_data['contents'],
                writer=user,
            )
            board.save()

            return redirect('/ceoboards/ceo_list')
    else:
        form = BoardForm()

    # 템플릿을 렌더링합니다.
    return render(request, 'ceo_board_write/ceo_board_write.html', {'form': form}) 

def ceo_board_detail(request, pk):
    board = get_list_or_404(Board, pk=pk)
    now = datetime.now()

    context = {
        "now": now,
        "board": board,
    }

    return render(request, 'ceo_board_detail/ceo_board_detail.html', context)

def ceo_board_list(request):
    try:
        page = int(request.GET.get('p', 1))
    except ValueError:
        page = 1

    all_boards = Board.objects.all().order_by('-id')
    paginator = Paginator(all_boards, 5)

    try:
        boards = paginator.get_page(page)
    except InvalidPage:
        boards = paginator.page(1)

    now = datetime.now()

    context = {
        "now": now,
        "boards": boards,
    }

    return render(request, 'ceo_board_list/ceo_board_list.html', context)