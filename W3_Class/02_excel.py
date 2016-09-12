# -*- coding: utf-8 -*-
"""
Created on 2016-09-09

@ Author: soma0sd
@ Disc: 데이터를 엑셀에 입력하고 저장하는 방법
@ License: MIT
@ 과제:
     - excel클래스의 cell_value와 cell_formula함수를 합친다.
     - 고려사항: 입력값에 '='가 제일 앞에 있으면 함수로 판단하는 엑셀의 특성을
             생각한다.
"""
import win32com.client  # 윈도우즈 클라이언트를 컨트롤하는 패키지


class excel:
    """
    클래스를 선언하면서 괄호를 사용하면, 클래스 내부의
    패키지, 클래스의 변수, 모듈, 함수, 클래스를 자유롭게 사용할 수 있다.
    """
    def __init__(self):
        """
        초기화 함수
        클래스를 선언하자마자 필요한 작업들
        """
        self._e = win32com.client.Dispatch("Excel.Application")
        # _e: 엑셀 어플리케이션
        self._wb = self._e.Workbooks.Add()
        # _wb: 워크북, 하나의 엑셀 파일을 지칭한다
        self._s = [self._wb.Worksheets("Sheet1")]
        # _s: 시트의 목록을 담는다
        self.select_sheet = self._wb.Worksheets("Sheet1")
        # select_sheet: 선택한 시트를 지정한다

    def visible(self, vis: bool=True):
        """
        편집중인 엑셀을 보여줄지 결정하는 함수.
        처음 선언했을때는 보이지 않는다.

        위의 vis: (type)=(val)은 (type)형태의 변수만 받고, 입력이 없으면,
        자동으로 (val)값으로 지정한다는 뜻
        """
        self._e.Visible = vis

    def sheet_add(self, name: str=''):
        """
        시트를 추가하는 함수
        추가한 시트는 자동으로 편집대상이 된다.
        """
        if name == '':
            name = 'Sheet' + str(len(self._s)+1)
        self._s.append(self._wb.Worksheets.Add())
        self._s[-1].Name = name
        self.select_sheet = self._s[-1]

    def sheet_get_list(self):
        """
        생성된 시트의 이름들을 list 변수형으로 출력한다
        """
        return [i.Name for i in self._s]

    def sheet_select(self, sheet_name=str):
        """
        시트의 이름으로 시트를 선택한다
        """
        self.select_sheet(self._wb.Worksheets(sheet_name))

    def cell_color(self, crow: int, ccol: int, cindex: int):
        """
        셀의 색상을 정한다. cindex 0-20까지 테스트 해보고 각각 어떤 색에
        매치되는지 알아보자
        """
        ws = self.select_sheet
        ws.Cells(crow, ccol).Interior.ColorIndex = cindex

    def cell_value(self, row: int, column: int, val=None):
        """
        셀에 값을 집어넣는 함수
        """
        ws = self.select_sheet
        if val is None:
            return ws.Cells(row, column).Value
        else:
            ws.Cells(row, column).Value = val

    def cell_formula(self, row: int, column: int, formula: str):
        """
        엑셀 함수를 셀에 집어넣고 싶을 때 이용하는 함수.
        ex. "=SUM(A:A)" 등.
        """
        ws = self.select_sheet
        ws.Cells(row, column).Formula = formula

    def columns_autofit(self):
        """
        열의 너비를 내용의 길이에 맞춰준다
        """
        ws = self.select_sheet
        ws.Columns.AutoFit()

    def save_excel(self, path: str):
        """
        만든 엑셀 파일을 저장하고 싶을 때 이용하는 함수
        """
        self._wb.SaveAs(path)

    def open_excel(self, path: str):
        """
        새로운 파일을 열고 싶을때 사용하는 함수
        """
        self._e.Workbooks.Open(path)

    def close(self):
        """
        엑셀 작업을 종료한다.
        """
        self._wb.Close()
        self._e.Application.Quit()

"""
본문
만든 클래스는 패키지처럼 이용할 수 있다
"""
e = excel()
e.visible()
e.cell_value(1, 1, "color")
for i in range(2, 30):
    e.cell_value(i, 1, i-2)
    e.cell_color(i, 1, i-2)
e.cell_formula(1, 2, "=SUM(A:A)")
e.columns_autofit()
