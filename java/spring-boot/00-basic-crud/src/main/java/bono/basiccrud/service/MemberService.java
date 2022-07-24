package bono.basiccrud.service;

import bono.basiccrud.domain.Member;
import bono.basiccrud.repository.MemberRepository;
import bono.basiccrud.repository.MemoryMemberRepository;

import java.util.List;
import java.util.Optional;

public class MemberService {
    private final MemberRepository memberRepository = new MemoryMemberRepository();


    // 회원 가입
    public Long join(Member member){
        // 중복 회원 이름 방지
        // Optional을 바로 반환하는걸 권장하지 않음
//        Optional<Member> result = memberRepository.findByName(member.getName());
//        result.ifPresent(mem ->{
//            throw new IllegalStateException("이미 존재하는 회원이다.")
//        });

        // ctrl + t -> Refactoring
        validateDuplicatedMember(member);

        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicatedMember(Member member) {
        memberRepository.findByName(member.getName())
                        .ifPresent(mem ->{
                            throw new IllegalStateException("이미 존재하는 회원입니다. ");
                        });
    }

    // 전체 회원 조회
    public List<Member> findMembers(){
        return memberRepository.findAll();
    }

    // 특정 회원 조회
    public Optional<Member> findMember(Long memberId){
        return memberRepository.findById(memberId);
    }
}
