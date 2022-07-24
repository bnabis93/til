package bono.basiccrud.service;

import bono.basiccrud.domain.Member;
import bono.basiccrud.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import  org.junit.jupiter.api.Test;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class MemberServiceTest {

    MemberService memberService;
    MemoryMemberRepository memberRepository;
    @BeforeEach
    public void beforeEach(){
        memberRepository = new MemoryMemberRepository();
        memberService = new MemberService(memberRepository);
    }

    @AfterEach
    public void afterEach(){
        // 각 test간의 의존성이 없어야한다.
        memberRepository.clearStore();
    }
    @Test
    void 회원가입() {
        // 중복회원가입 테스트
        // given
        Member member = new Member();
        member.setName("bono");


        // when
        Long savedId = memberService.join(member);

        // then
        Member findMember = memberService.findMember(savedId).get();
        assertThat(member.getName()).isEqualTo(findMember.getName());
    }

    @Test
    public void 중복회원예외(){
        // 중복된 회원이 존재 할 떄, 예외를 터트리는지 확인한다.
        // given
        Member member01 = new Member();
        member01.setName("bono");
        Member member02 = new Member();
        member02.setName("bono");
        // when
        memberService.join(member01);
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member02));
        assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
//        try{
//            memberService.join(member02 );
//            fail("예외 발생");
//        }catch (IllegalStateException e){
//            assertThat(e.getMessage() ).isEqualTo("이미 존재하는 회원입니다.");
//        }

        // then

    }


    @Test
    void findMembers() {
    }

    @Test
    void findMember() {
    }
}