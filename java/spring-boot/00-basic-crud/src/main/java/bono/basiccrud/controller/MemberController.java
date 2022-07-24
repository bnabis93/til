package bono.basiccrud.controller;

import bono.basiccrud.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

// Spring bean이 관리된다.
// Spring 프로젝트 빌드 후 실행 -> spring 컨테이너가 뜨는데, 특정 annotation 들은 spring 이 관리함. 이를 보고 bean이 관리된다고 한다.
@Controller
public class MemberController {

    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
}
