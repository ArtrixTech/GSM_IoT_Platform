def make_chart(device_id):

    _MAX_LABEL_ = 15

    sensor = clients[device_id]
    assert isinstance(sensor, Client)
    assert isinstance(sensor.dust, list)
    assert isinstance(sensor.humi, list)
    assert isinstance(sensor.temp, list)
    assert isinstance(sensor.pres, list)
    import pygal

    def get_times():

        ret_list = list()
        assert isinstance(sensor.dust, list)
        rev_list = sensor.dust
        rev_list.reverse()
        time_count = 0
        for i in rev_list:
            if time_count >= _MAX_LABEL_:
                break
            ret_list.append(int(i["time"]))
            time_count+=1
        return ret_list

    def get_dust():

        ret_list = list()
        assert isinstance(sensor.dust, list)
        rev_list = sensor.dust
        rev_list.reverse()
        time_count = 0
        for i in rev_list:
            if time_count >= _MAX_LABEL_:
                break
            ret_list.append(int(i["argument"]))
            time_count += 1
        return ret_list

    def get_temp():

        ret_list = list()
        assert isinstance(sensor.temp, list)
        rev_list = sensor.temp
        rev_list.reverse()
        time_count = 0
        for i in rev_list:
            if time_count >= _MAX_LABEL_:
                break
            ret_list.append(float(i["argument"]))
            time_count += 1
        return ret_list

    def get_humi():

        ret_list = list()
        assert isinstance(sensor.humi, list)
        rev_list = sensor.humi
        rev_list.reverse()
        time_count = 0
        for i in rev_list:
            if time_count >= _MAX_LABEL_:
                break
            ret_list.append(float(i["argument"]))
            time_count += 1
        return ret_list

    def get_pres():

        ret_list = list()
        assert isinstance(sensor.pres, list)
        rev_list = sensor.pres
        rev_list.reverse()
        time_count = 0
        for i in rev_list:
            if time_count >= _MAX_LABEL_:
                break
            ret_list.append(float(i["argument"]))
            time_count += 1
        return ret_list

    line_chart_temp = pygal.Line()
    line_chart_temp.title = 'Artrix Cloud Service - Device ' + device_id
    line_chart_temp.x_labels = get_times()
    line_chart_temp.add('Temperature', get_temp())

    line_chart_pres = pygal.Line()
    line_chart_pres.title = 'Artrix Cloud Service - Device ' + device_id
    line_chart_pres.x_labels = get_times()
    line_chart_pres.add('Pressure', get_pres())

    line_chart_dust = pygal.Line()
    line_chart_dust.title = 'Artrix Cloud Service - Device ' + device_id
    line_chart_dust.x_labels = get_times()
    line_chart_dust.add('Dust', get_dust())

    line_chart_humi = pygal.Line()
    line_chart_humi.title = 'Artrix Cloud Service - Device ' + device_id
    line_chart_humi.x_labels = get_times()
    line_chart_humi.add('Humidity', get_humi())

    t = open('temp.html', 'wb')
    h = open('humi.html', 'wb')
    p = open('pres.html', 'wb')
    d = open('dust.html', 'wb')

    t.write(line_chart_temp.render())
    t.close()

    h.write(line_chart_humi.render())
    h.close()

    p.write(line_chart_pres.render())
    p.close()

    d.write(line_chart_dust.render())
    d.close()