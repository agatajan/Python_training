# -------------------------------------------------------------------------------
# Name:        turkey_ad_sdv
# Purpose:
#
# Author:      Ingest GDN Team
#
# Created:     23/04/2018
# Copyright:   (c) Jeppesen
# Licence:     <your licence>
# Functions Varsion:     0.1.9
# SDV Code Varsion:     1.0.1
# History:     Updated > 05/08/2019 > 0.1 DSDTP-15969
#
#
# -------------------------------------------------------------------------------

import fme
import fmeobjects
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class FeatureProcessor(object):
    def __init__(self):
        pass

    def input(self, feature):
        self.log_counter = 0

        # Attribute Collection
        feature.setAttribute('log_code', '0')
        attrib_list = feature.getAllAttributeNames()
        attrib_collection = {}
        for attrib in attrib_list:
            attrib_collection[attrib] = feature.getAttribute(attrib)

        user_attrib_collection = inputColumns
        user_attrib_values = []
        for attrib in user_attrib_collection:
            value = feature.getAttribute(attrib)
            user_attrib_values.append(value)

        # Attributes names
        obs_name = 'OBSTACLENO'
        obs_type_name = 'OBSTACLETYPE'
        lat_name = 'LATITUDE'
        long_name = 'LONGITUDE'
        elev_m_name = 'OBSTACLEELEVATIONAMSLm'
        hgt_m_name = 'HEIGHTOFOBSTACLEAGLm'
        location_elevation_msl_m_name = 'GROUNDLEVELATOBSTACLEm'
        lgt_name = 'LITSTATUS'
        lgt_color_name = 'COLOUR'
        group_name = 'Group'

        # Attributes
        # obs = str(attrib_collection.get(obs_name))
        # obs_type = str(attrib_collection.get(obs_type_name))
        lat = str(attrib_collection.get(lat_name))
        long = str(attrib_collection.get(long_name))
        elev_m = str(attrib_collection.get(elev_m_name))
        hgt_m = str(attrib_collection.get(hgt_m_name))
        base_m = str(attrib_collection.get(location_elevation_msl_m_name))
        # lgt = str(attrib_collection.get(lgt_name))
        # lgt_color = str(attrib_collection.get(lgt_color_name))
        # group = str(attrib_collection.get(group_name))

        # FME_Attributes
        # source_id = (str(feature.getAttribute('OBSTACLENO'))).rstrip(".0")
        source_id = str(int(feature.getAttribute('OBSTACLENO')))
        row_number = str(feature.getAttribute('xlsx_row_id') - 1)
        job_id = str(feature.getAttribute('job_id'))
        fme_job_id = str(FME_MacroValues['FME_JOB_ID'])
        duplicate_flag = str(feature.getAttribute('duplicate_flag'))
        duplicate_sourceid_flag = str(feature.getAttribute('duplicate_sourceid_flag'))
        uuid = str(feature.getAttribute('vs_uuid'))
        feature_type = 'POINT'
        swm_job_id = str(feature.getAttribute('smartWfmSourceIdentifier'))

        print(source_id)

        # Variables
        log_id = 'SF_RF_'
        status_h = 'HIGH'
        status_m = 'MEDIUM'
        status_l = 'LOW'
        regex1 = '^(?i)(\s*)([0]*)(([0-9]{6})([.])([0-9]+)|([0-9]{6}))([N,S])(\s*)$'
        regex2 = '^(?i)(\s*)([0]*)(([0-9]{6,7})([.])([0-9]+)|([0-9]{6,7}))([E,w])(\s*)$'

        # Logs
        sep = '|'
        null = ''
        info_check = 'Check Value'
        info_null = 'NULL or EMPTY value'
        info_ehb = 'No elevation, height and base'
        info_duprec = 'RECORD DUPLICATED'
        info_dupsourcerec = 'RECORD WITH DUPLICATED source_id'
        info_wrongrec = 'WRONG ATTRIBUTES AMOUNT'
        info_ue = 'UNKNOWN ERROR'

        log_list = [sep, log_id, job_id, null, null, source_id, row_number, null, null, null, fme_job_id, uuid,
                    feature_type, swm_job_id]
        log_list_ue = [sep, log_id, job_id, null, null, null, row_number, null, null, null, fme_job_id, null, null,
                       swm_job_id]
        log_list_error = [sep, log_id, job_id, null, null, source_id, row_number, null, null, null, fme_job_id, uuid,
                          null, swm_job_id]

        def is_number(s, date_type='float'):
            try:
                if date_type == 'int':
                    if isinstance(s, (int, long)):
                        return True
                    else:
                        return float(s).is_integer()
                else:
                    float(s)
                    return True
            except ValueError:
                return False

        def is_between_values(f, limit):
            try:
                return -limit < float(f) < limit
            except ValueError:
                return False

        def recreate_list(input_list, status, attr_name, var, info):
            output_list = list(input_list)
            output_list[3] = self.log_counter
            output_list[4] = status
            output_list[7] = attr_name
            if var not in ['', ' ', 'Unknown', None, 'None']:
                output_list[8] = var.splitlines()[0]
            else:
                output_list[8] = var
            output_list[9] = info
            return output_list

        def logging(log_data):
            try:
                loggs = len(log_data)
                if loggs == 14:
                    return (
                        '{13}{0}{1}{2}_{6}{3}{0}{4}{0}{5}{0}{6}{0}{7}{0}{8}{0}{9}{0}{2}{0}{10}{0}{11}{0}{12}'.format(
                            *log_data))
                else:
                    return False
            except ValueError:
                return False

        # Validation Rules
        def regex_vr(status, attr_name, var, regex, nullable):
            try:
                if var not in ['', 'None', None]:
                    if not bool(re.match(regex, str(var))):
                        feature.setAttribute('log_code', '1')
                        self.log_counter += 1
                        return logging(recreate_list(log_list, status, attr_name, var, info_check))
                    else:
                        return 'pass'
                else:
                    if nullable:
                        return 'pass'
                    else:
                        feature.setAttribute('log_code', '1')
                        self.log_counter += 1
                        return logging(recreate_list(log_list, status, attr_name, var, info_null))
            except (AttributeError, TypeError, NameError, ValueError, UnicodeError, IndexError):
                feature.setAttribute('log_code', '1')
                self.log_counter += 1
                return logging(recreate_list(log_list_ue, status_h, null, null, info_ue))

        def number_type_vr(status, attr_name, var, limit, nullable, data_type='float'):
            try:
                if var not in ['', 'None', None]:
                    if not is_number(var, data_type):
                        feature.setAttribute('log_code', '1')
                        self.log_counter += 1
                        return logging(recreate_list(log_list, status, attr_name, var, info_check))
                    elif not (is_between_values(var, limit)):
                        feature.setAttribute('log_code', '1')
                        self.log_counter += 1
                        return logging(recreate_list(log_list, status, attr_name, var, info_check))
                    else:
                        return 'pass'
                else:
                    if nullable:
                        return 'pass'
                    else:
                        feature.setAttribute('log_code', '1')
                        self.log_counter += 1
                        return logging(recreate_list(log_list, status, attr_name, var, info_null))
            except (AttributeError, TypeError, NameError, ValueError, UnicodeError, IndexError):
                feature.setAttribute('log_code', '1')
                self.log_counter += 1
                return logging(recreate_list(log_list_ue, status_h, null, null, info_ue))

        def string_type_vr(status, attr_name, var, length, nullable, equation='='):
            try:
                if var not in ['', 'None', None]:
                    if equation == '=':
                        if not len(var) == length:
                            feature.setAttribute('log_code', '1')
                            self.log_counter += 1
                            return logging(recreate_list(log_list, status, attr_name, var, info_check))
                        else:
                            return 'pass'
                    elif equation == '<':
                        if not len(var) < length:
                            feature.setAttribute('log_code', '1')
                            self.log_counter += 1
                            return logging(recreate_list(log_list, status, attr_name, var, info_check))
                        else:
                            return 'pass'
                    else:
                        return 'pass'
                else:
                    if nullable:
                        return 'pass'
                    else:
                        feature.setAttribute('log_code', '1')
                        self.log_counter += 1
                        return logging(recreate_list(log_list, status, attr_name, var, info_null))
            except (AttributeError, TypeError, NameError, ValueError, UnicodeError, IndexError):
                feature.setAttribute('log_code', '1')
                self.log_counter += 1
                return logging(recreate_list(log_list_ue, status_h, null, null, info_ue))

        def elev_hgt_base_vr(status, attributes_var):
            attributes = ''
            values = ''
            try:
                for (att, var) in attributes_var:
                    if var not in ['', 'None', None] and is_number(var):
                        return 'pass'
                    else:
                        if var is None:
                            var = ''
                        if attributes == '':
                            attributes += str(att)
                        else:
                            attributes += ' {0}'.format(att)
                        if values == '':
                            values += str(var)
                        else:
                            values += ' {0}'.format(var)
                if attributes:
                    feature.setAttribute('log_code', '1')
                    self.log_counter += 1
                    return logging(recreate_list(log_list, status, attributes, values, info_ehb))
            except (AttributeError, TypeError, NameError, ValueError, UnicodeError, IndexError):
                feature.setAttribute('log_code', '1')
                self.log_counter += 1
                return logging(recreate_list(log_list_ue, status_h, null, null, info_ue))

        def errorrec_vr(info):
            try:
                feature.setAttribute('log_code', '1')
                self.log_counter += 1
                return logging(recreate_list(log_list_error, status_h, null, null, info))
            except (AttributeError, TypeError, NameError, ValueError, UnicodeError, IndexError):
                feature.setAttribute('log_code', '1')
                self.log_counter += 1
                return logging(recreate_list(log_list_ue, status_h, null, null, info_ue))

        # Logs Collection
        logger = fmeobjects.FMELogFile()

        logs_collection = []

        empty_record_flag = False

        user_attrib_values_set = set(user_attrib_values)
        if user_attrib_values_set == {'', None} or user_attrib_values_set == {''} or user_attrib_values_set == {None}:
            empty_record_flag = True
        else:
            if duplicate_flag == '1':
                logs_collection.append(errorrec_vr(info_duprec))
            else:
                if duplicate_sourceid_flag == '1':
                    logs_collection.append(errorrec_vr(info_dupsourcerec))
                # obs is not checked
                # obs_type is not populated
                logs_collection.append(regex_vr(status_h, lat_name, lat, regex1, False))
                logs_collection.append(regex_vr(status_h, long_name, long, regex2, False))
                logs_collection.append(number_type_vr(status_h, elev_m_name, elev_m, 1.797 * (10 ** 308), True))
                logs_collection.append(number_type_vr(status_h, hgt_m_name, hgt_m, 1.797 * (10 ** 308), True))
                logs_collection.append(
                    number_type_vr(status_h, location_elevation_msl_m_name, base_m, 1.797 * (10 ** 308), True))
                # lgt is not checked
                # lgt_color is not checked
                # group is not checked
                logs_collection.append(elev_hgt_base_vr(status_h, [(elev_m_name, elev_m), (hgt_m_name, hgt_m)]))

        if not empty_record_flag:
            logs_collection2 = [log for log in logs_collection if log != 'pass']
            feature.setAttribute('log_counter', str(len(logs_collection2)))

            # Logs print in FME log file and in fme_log table
            for log in logs_collection2:
                logger.logMessageString(log, fmeobjects.FME_WARN)

            feature.setAttribute('row_number', row_number)
            feature.setAttribute('feature_type', feature_type)
            feature.setAttribute('swm_job_id', swm_job_id)
            self.pyoutput(feature)

    def close(self):
        pass
