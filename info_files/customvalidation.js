/*
 * httpsprefix
 */
$.validator.addMethod("httpsprefix",
    function (value) {

        if (value.length == 0 || value.substring(0,8) == "https://") {
            return true;
        }
        else {
            return false;
        }
    });

$.validator.unobtrusive.adapters.addBool("httpsprefix");


/*
 * GreaterThan
 */
$.validator.addMethod("greaterthan",
    function (value1, element, params) {
        var value2 = $("#" + params.compareProperty).val();

        // if required, required method will handle.
        if (value1 === '' || value2 === '') {
            return true;
        }

        // compare number
        if (!isNaN(value1) && !isNaN(value2) && parseInt(value1) > parseInt(value2)) {
            return true;
        }

        // compare date
        var date1 = new Date(value1);
        var date2 = new Date(value2);
        if (isValidDate(date1) && isValidDate(date2) && date1 > date2) {
            return true;
        }

        // compare time
        var time1 = new Date("01/01/2020 " + value1);
        var time2 = new Date("01/01/2020 " + value2);
        if (isValidDate(time1) && isValidDate(time2) && time1 > time2) {
            return true;
        }

        return false;
    });

$.validator.unobtrusive.adapters.add('greaterthan', ['compare'], function (options) {
    options.rules['greaterthan'] = { compareProperty: options.params.compare };
    options.messages['greaterthan'] = options.message;
});

function isValidDate(d) {
    return d instanceof Date && !isNaN(d);
}

/*
 * RequiredIfTrue
 */
$.validator.addMethod("requiredif",
    function (value, element, params) {
        var $element = $("#" + params.compareProperty);
        var elementType = $element.attr('type');
        var actualvalue =
            elementType === 'checkbox' ?
                $element.attr('checked').toString() :
                $element.val();

        var targetValue = params.targetValue;
        if (actualvalue !== null && actualvalue !== undefined &&
            actualvalue.toLowerCase() === targetValue.toLowerCase()) {
            return $.validator.methods.required.call(this, value, element, params);
        }
        return true;
    }
);
$.validator.unobtrusive.adapters.add('requiredif', ['compare', 'targetValue'], function (options) {
    options.rules['requiredif'] = { compareProperty: options.params.compare, targetValue: options.params.targetValue };
    options.messages['requiredif'] = options.message;
});


/*
 * RequiredIfNotNull
 */
$.validator.addMethod("requiredifnotnull",
    function (value, element, params) {
        var otherValue = $("#" + params.compareProperty).val();
        if ((otherValue !== null && otherValue !== undefined && otherValue) &&
            (value === null || value === undefined || value.trim() === '')) {
            return $.validator.methods.required.call(this, value, element, params);
        }
        return true;
    }
);
$.validator.unobtrusive.adapters.add('requiredifnotnull', ['compare'], function (options) {
    options.rules['requiredifnotnull'] = { compareProperty: options.params.compare };
    options.messages['requiredifnotnull'] = options.message;
});