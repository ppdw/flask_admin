; (function ($, w, d) {
    var z7 = w["z7"] = {};

    z7.mobile = {
        android: function () {
            return navigator.userAgent.match(/Android/i) ? true : false;
        },
        blackBerry: function () {
            return navigator.userAgent.match(/BlackBerry/i) ? true : false;
        },
        ios: function () {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i) ? true : false;
        },
        windows: function () {
            return navigator.userAgent.match(/IEMobile/i) ? true : false;
        },
        any: function () {
            return (z7.mobile.android() || z7.mobile.blackBerry() || z7.mobile.ios() || z7.mobile.windows());
        },
        pc: function () {
            var userAgentInfo = navigator.userAgent;
            var Agents = new Array("Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod");
            var flag = true;
            for (var v = 0; v < Agents.length; v++) {
                if (userAgentInfo.indexOf(Agents[v]) > 0) { flag = false; break; }
            }
            return flag;
        },
        wechat: function () {
            var ua = window.navigator.userAgent.toLowerCase();
            if (ua.match(/MicroMessenger/i) == 'micromessenger') {
                return true;
            } else {
                return false;
            }
        }
    };

})(jQuery, window, document);

$(function () {
    if (z7.mobile.wechat()) {
        var dialog = '<div class="tcdialong" id="tcdialong"><div class="arrow"><img src="images/wechat/arrow.png"></div><div class="explain"><img src="images/wechat/explain.png"></div><div class="getBtn" id="get"><a href="javascript:void(0);"><img src="images/wechat/getBtn.png"></a></div></div>';
        $("body").append(dialog);
    }

    //自动识别IOS和安卓系统
    if (z7.mobile.ios()) {
        $(".ios_download").show();
        $(".az_download").hide();
    }
    else {
        $(".az_download").show();
        $(".ios_download").hide();
    }

    $("#get").click(function () {
        $("#tcdialong").fadeOut(300, function () {
            $(this).remove();
        });
    });
});