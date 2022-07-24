package bono.basiccrud.controller;

import bono.basiccrud.domain.Member;
import bono.basiccrud.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

// Spring bean이 관리된다.
// Spring 프로젝트 빌드 후 실행 -> spring 컨테이너가 뜨는데, 특정 annotation 들은 spring 이 관리함. 이를 보고 bean이 관리된다고 한다.

//@RestController
@Controller
public class MemberController {

    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/members/new")
    public String createForm(){
        return "members/createMemberForm";
    }

    @PostMapping("/members/new")
    public String create(MemberForm form){
        Member member = new Member();
        member.setName(form.getName());

        memberService.join(member);

        return "redirect:/";
    }

    @GetMapping("/members")
    public String list(Model model){
        List<Member> members = memberService.findMembers();
        model.addAttribute("members" , members);
        return "members/memberList";
    }

    @ResponseBody
    @PostMapping("/members/create")
    public String createMember(@RequestBody Member mem){
        Member member = new Member();
        System.out.println("mem name : " +mem.getName() );
        member.setName(mem.getName());
        memberService.join(member);
        return "Member created";
    }

    @ResponseBody
    @GetMapping("/members/list")
    public String getMembers(){
        List<Member> members = memberService.findMembers();
        List<String> memberLists = new ArrayList<>();
        for (Member member : members){
            memberLists.add(member.getName());
        }
        return memberLists.toString();
    }
}
