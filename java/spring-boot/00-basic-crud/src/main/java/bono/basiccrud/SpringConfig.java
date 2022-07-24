package bono.basiccrud;


import bono.basiccrud.repository.MemberRepository;
import bono.basiccrud.repository.MemoryMemberRepository;
import bono.basiccrud.service.MemberService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/*
Spring Bean을 manually 하게 등록하는 방법.
 */
@Configuration
public class SpringConfig {
    @Bean
    public MemberService memberService(){
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository(){
        return new MemoryMemberRepository();
    }
}
