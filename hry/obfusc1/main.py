# -*- coding: utf-8 -*-
import sys
l1ll11l_opy_ = sys.version_info [0] == 2
l11l1_opy_ = 2048
l1ll1l1_opy_ = 7
def l1llll_opy_ (l1l111_opy_):
    global l111_opy_
    l1lll1l_opy_ = ord (l1l111_opy_ [-1])
    l11l_opy_ = l1l111_opy_ [:-1]
    l111l_opy_ = l1lll1l_opy_ % len (l11l_opy_)
    l1l1l11_opy_ = l11l_opy_ [:l111l_opy_] + l11l_opy_ [l111l_opy_:]
    if l1ll11l_opy_:
        l11ll_opy_ = l111ll_opy_ () .join ([l1ll1ll_opy_ (ord (char) - l11l1_opy_ - (l1ll_opy_ + l1lll1l_opy_) % l1ll1l1_opy_) for l1ll_opy_, char in enumerate (l1l1l11_opy_)])
    else:
        l11ll_opy_ = str () .join ([chr (ord (char) - l11l1_opy_ - (l1ll_opy_ + l1lll1l_opy_) % l1ll1l1_opy_) for l1ll_opy_, char in enumerate (l1l1l11_opy_)])
    return eval (l11ll_opy_)
from easygame import *
import math
from random import randint
def l11l11_opy_(u, v):
    (l1lll1_opy_, l1_opy_) = u
    (l1lll11_opy_, l1111_opy_) = v
    return math.hypot(l1lll1_opy_-l1lll11_opy_, l1_opy_-l1111_opy_)
#l1ll1_opy_ l1l1ll_opy_
l11ll1_opy_ = load_image(l1llll_opy_ (u"ࠫࡦࡶࡰ࡭ࡧ࠱ࡴࡳ࡭ࠧࠀ"))
l1l1l_opy_ = load_image(l1llll_opy_ (u"ࠬࡶࡡࡴࡶࡤ࠲ࡵࡴࡧࠨࠁ"))
l111l1_opy_ = load_image(l1llll_opy_ (u"࠭ࡣࡰ࡭ࡲࡰࡦࡪࡡ࠯ࡲࡱ࡫ࠬࠂ"))
#l1ll111_opy_
l1ll11_opy_ = 5
l1111l_opy_ = 4
l1lllll_opy_ = 50
l1l11_opy_ = 50
#l11l1l_opy_ l1l11ll_opy_ l11lll_opy_
l1lll_opy_ = 0
l1l1ll1_opy_ = (50,50)
l11_opy_ = (randint(0,400),500)
l1l_opy_ = False
ll_opy_ = False
l1l1l1_opy_ = False
l1l1lll_opy_ = False
#l11111_opy_ l1l11l_opy_
open_window(l1llll_opy_ (u"ࠧࡉࡴࡤࠫࠃ"), 600, 400)
l1l1l1l_opy_ = False
while not l1l1l1l_opy_:
    for l1l1_opy_ in poll_events():
        if type(l1l1_opy_) is CloseEvent:
            l1l1l1l_opy_ = True
        if type(l1l1_opy_) is KeyDownEvent:
            if l1l1_opy_.key == l1llll_opy_ (u"ࠨࡎࡈࡊ࡙࠭ࠄ"):
                l1l_opy_ = True
            if l1l1_opy_.key == l1llll_opy_ (u"ࠩࡕࡍࡌࡎࡔࠨࠅ"):
                ll_opy_ = True
            if l1l1_opy_.key == l1llll_opy_ (u"ࠪࡗࡕࡇࡃࡆࠩࠆ"):
                l1l1l1_opy_ = True
        if type(l1l1_opy_) is KeyUpEvent:
            if l1l1_opy_.key == l1llll_opy_ (u"ࠫࡑࡋࡆࡕࠩࠇ"):
                l1l_opy_ = False
            if l1l1_opy_.key == l1llll_opy_ (u"ࠬࡘࡉࡈࡊࡗࠫࠈ"):
                ll_opy_ = False
            if l1l1_opy_.key == l1llll_opy_ (u"࠭ࡓࡑࡃࡆࡉࠬࠉ"):
                l1l1l1_opy_ = False
    #
    if l1lll_opy_ < 10:
        (l1ll1l_opy_, l1llll1_opy_) = l1l1ll1_opy_
        if l1l_opy_:
            l1ll1l_opy_ -= l1ll11_opy_
        if ll_opy_:
            l1ll1l_opy_ += l1ll11_opy_
        l1l1ll1_opy_= (l1ll1l_opy_, l1llll1_opy_)
        l11_opy_=(l11_opy_[0],l11_opy_[1]-l1111l_opy_)
        if l11l11_opy_(l1l1ll1_opy_, l11_opy_) <= l1lllll_opy_:
            l1lll_opy_ = l1lll_opy_+1
            l11_opy_ = (randint(0,400),500)
        if l11_opy_[1] < 0:
            l1l1lll_opy_ = True
    #
    l1l111l_opy_ = (l1l1ll1_opy_[0]+50,l1l1ll1_opy_[1])
    fill(255,255,255)
    draw_image(l11ll1_opy_,l11_opy_,scale=0.8)
    draw_line(l1l1ll1_opy_, (l1l1ll1_opy_[0]+1,l1l1ll1_opy_[1]), l1l111l_opy_, thickness = 10, color = (0,0,0,1))
    draw_text(l1llll_opy_ (u"ࠧࡄࡪࡼ३ࠥ࠷࠰ࠡ࡬ࡤࡦिࡱ࠮ࠨࠊ"),l1llll_opy_ (u"ࠨࡖ࡬ࡱࡪࡹࠠࡏࡧࡺࠤࡗࡵ࡭ࡢࡰࠪࠋ"), 10, position=(50,350), color=(0,0,0,1))
    if l1l1l1_opy_:
        draw_image(l111l1_opy_, position =(300,200),scale=0.8)
    if l1lll_opy_>=10:
        draw_image(l1l1l_opy_, position=(300,200), scale=0.8)
        draw_text(l1llll_opy_ (u"ࠩ࡜ࡓ࡚ࠦࡗࡊࡐࠤࠫࠌ"), l1llll_opy_ (u"ࠪࡘ࡮ࡳࡥࡴࠢࡑࡩࡼࠦࡒࡰ࡯ࡤࡲࠬࠍ"), 32, position=(50,50), color=(0,0,1,1), bold = True)
    if l1l1lll_opy_:
        draw_text(l1llll_opy_ (u"ࠫࡕࡸࡥࡩࡴࡤࡰࠥࡹࡩࠨࠎ"), l1llll_opy_ (u"࡚ࠬࡩ࡮ࡧࡶࠤࡓ࡫ࡷࠡࡔࡲࡱࡦࡴࠧࠏ"), 32, position=(50,50), color=(0,0,1,1), bold = True)
    #
    next_frame()
close_window()