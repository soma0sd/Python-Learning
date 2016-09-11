# -*- coding: utf-8 -*-
"""
Created on 2016-09-09

@ Author: soma0sd
@ Disc: 데이터를 엑셀에 입력하는 방법
@ License: MIT
"""
import win32com.client  # 윈도우즈 클라이언트를 컨트롤하는 패키지


class excel:
    """
    클래스를 선언하면서 괄호를 사용하면, 클래스 내부의
    패키지, 클래스의 변수, 모듈, 함수, 클래스를 자유롭게 사용할 수 있다.
    """
    def __init__(self):
        self._e = win32com.client.Dispatch("Excel.Application")
        self._wb = self._e.Workbooks.Add()
        self._s = [self._wb.Worksheets("Sheet1")]

    def sheet_add(self, name: str=''):
        if name == '':
            name = 'Sheet' + str(len(self._s)+1)
        self._s.append(self._wb.Worksheets.Add())
        self._s[-1].Name = name

    def sheet_get_list(self):
        return [i.Name for i in self._s]

    def test(self):
        ws = self._s[0]
        ws.Cells(1, 1).Value = "Cell A1"
        ws.Cells(1, 1).Offset(2, 4).Value = "Cell D2"
        ws.Range("A2").Value = "Cell A2"
        ws.Range("A3:B4").Value = "A3:B4"
        ws.Range("A6:B7,A9:B10").Value = "A6:B7,A9:B10"
        for i in range(1, 21):
            ws.Cells(i, 5).Value = i
            ws.Cells(i, 5).Interior.ColorIndex = i
        ws.Range(ws.Cells(3, 1), ws.Cells(3, 4)).Value = [5, 6, 7, 8]
        ws.Range("A4:D4").Value = [i for i in range(9, 13)]
        ws.Cells(5, 4).Formula = '=SUM(A2:D4)'
        ws.Cells(5, 4).Font.Size = 16
        ws.Cells(5, 4).Font.Bold = True
        ws.Columns.AutoFit()


e = excel()
e.test()
e._e.Visible = True
