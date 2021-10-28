var DateRangePickerExt = function (options) {
    var defaultSetting = {
        start: moment().subtract(1, 'months'),
        end: moment(),
        bindTo: '#daterange',
        change: function (start, end) {
            console.log('change date range:', { 'start': start, 'end': end });
        }
    };
    var config = $.extend({}, defaultSetting, options);

    var self = this;

    self.load = function () {
        $(config.bindTo).daterangepicker({
            startDate: config.start,
            endDate: config.end,
            ranges: {
                'Today': [moment(), moment()],
                'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
                'Last 7 Days': [moment().subtract(7, 'days'), moment()],
                'Past month': [moment().subtract(1, 'months'), moment()],
                'This Month': [moment().startOf('months'), moment()],
                'Last Month': [moment().subtract(1, 'months').startOf('month'), moment().subtract(1, 'months').endOf('month')],
                'This Year': [moment().startOf('years').startOf('year'), moment()],
                'Last Year': [moment().subtract(1, 'years').startOf('year'), moment().subtract(1, 'years').endOf('year')],
                'All Data': [moment([2017, 0, 1]), moment()]
            }
        }, function (start, end) {
            config.change(start, end);
        });
    };
    return self;
};

function modalConfirm(message, yesCallback, noCallback, options) {
    if (typeof (message) === 'object') {
        options = message;
    }
    if (options === undefined) {
        options = {};
    }

    var defaultOptions = {
        message: message,
        yesTitle: "OK",
        yesCallback: yesCallback,
        noTitle: "Cancel",
        noCallback: noCallback
    };
    options = $.extend(defaultOptions, options);

    $('<div class="modal fade" id="modal_confirm" tabindex="-1" role="dialog" aria-labelledby="modal_confirm" aria-hidden="true">           <div class="modal-dialog" role="document">                <div class="modal-content">                    <div>                        <div class="modal-header">                            <h3 class="modal-title" id="modal_confirm_title">'
        +options.message+'</h3>                        </div>                        <div class="modal-footer">                            <button type="button" id="btnYes" class="btn btn-primary" data-dismiss="modal" aria-label="OK">                                <span aria-hidden="true">'
        +options.yesTitle +'</span>                            </button>                            <button type="button" id="btnNo" class="btn btn-default" data-dismiss="modal" aria-label="Cancel">                                <span aria-hidden="true">'
        +options.noTitle +'</span>                            </button>                        </div>                    </div>                </div>            </div>        </div>')
        .appendTo('body');

    var $confirm = $('#modal_confirm');
    $confirm.modal({ backdrop: 'static', keyboard: false });

    $confirm.find('#btnYes').click(function (e) {
        e.preventDefault();
        $confirm.modal('hide');
        if (options.yesCallback !== undefined && typeof (options.yesCallback) === 'function')
            options.yesCallback();
    });
    $confirm.find('#btnNo').click(function (e) {
        e.preventDefault();
        $confirm.modal('hide');
        if (options.noCallback !== undefined && typeof (options.noCallback) === 'function')
            options.noCallback();
    });

    $confirm.on('hidden.bs.modal', function (e) {
        e.preventDefault();
        $confirm.remove();
    });
}

function modalAlert(message, okCallback, showCancel) {
    var cancelButton='';
    if (showCancel) {
        cancelButton = '<button type="button" id="btnCancel" class="btn btn-default" data-dismiss="modal" aria-label="Cancel">  Cancel </button>  ';
    }

    $('<div class="modal fade" id="modal_alert" tabindex="-1" role="dialog" aria-labelledby="modal_confirm" aria-hidden="true">            <div class="modal-dialog" role="document">                <div class="modal-content">                    <div>                        <div class="modal-header">                            <h3 class="modal-title" id="modal_confirm_title">'+message+'</h3>                        </div>                                        <div class="modal-footer">                            <button type="button" id="btnOk" class="btn btn-default" data-dismiss="modal" aria-label="OK">                                <span aria-hidden="true"> OK </span>                            </button>        '+cancelButton+'                </div>                    </div>                </div>            </div>        </div>')
     .appendTo('body');

    var $alert = $('#modal_alert');
    $alert.modal({ backdrop: 'static', keyboard: false });

    $alert.find('#btnOk').click(function (e) {
        e.preventDefault();
        $alert.modal('hide');
        if (okCallback !== undefined && typeof (okCallback) === 'function')
            okCallback();
    });

    $alert.on('hidden.bs.modal', function (e) {
        e.preventDefault();
        $alert.remove();
    });
}

jQuery.fn.serializeObject = function () {
    var data = {};
    $(this).serializeArray().map(function (x) {
        if (!data.hasOwnProperty(x.name)) {
            data[x.name] = x.value;
        }
    }); 
    return data;
};

function toggleResponsiveMenu() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
